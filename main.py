from itertools import islice
import heap

# nodeId.edges : The edges in the ego network for the node 'nodeId'. Edges are
#   undirected for facebook, and directed (a follows b) for twitter and gplus.
#   The 'ego' node does not appear, but it is assumed that they follow every
#   node id that appears in this file.
# nodeId.circles : The set of circles for the ego node. Each line contains one
#   circle, consisting of a series of node ids. The first entry in each line is
#   the name of the circle.
# nodeId.feat : The features for each of the nodes that appears in the edge
#   file.
# nodeId.egofeat : The features for the ego user.
# nodeId.featnames : The names of each of the feature dimensions. Features are
#   '1' if the user has this property in their profile, and '0' otherwise.
#   This file has been anonymized for facebook users, since the names of the
#   features would reveal private data

def take(n, iterable):
  # Return first n items of the iterable as a list
  return list(islice(iterable, n))

def createGraphFromFile(filePath):
  fp = open(filePath, 'r')
  egoGraph = {}
  for line in fp:
    ln = line.split(' ')
    # Removing whitespaces from text in file
    ln[1] = ln[1].replace('\n', '').strip()
    # Converting to number will make it easier to store in memory
    ln[0] = int(ln[0])
    ln[1] = int(ln[1])
    if ln[0] in egoGraph:
      egoGraph[ln[0]].append(ln[1])
    else:
      egoGraph[ln[0]] = [ln[1]]
  return egoGraph

def get100BiggestInfluencers(L):
    followerCount = {}
    for account in L:
        if account in followerCount:
            followerCount[account] += 1
        else:
            followerCount[account] = 1
    hp = heap.heap()
    for key in followerCount:
        hp.insert(heap.node(key, followerCount[key]))
    ret = []
    for i in range(100):
        ret.append(hp.extractMax())
    return ret
    
    
def main(filePath):
  twitterGraph = createGraphFromFile(filePath)
  print(take(1, twitterGraph.items()))
  following = list(twitterGraph.values())
  following_flattened = [node for sublist in following for node in sublist]
  biggest100Influencers = get100BiggestInfluencers(following_flattened)
  for i in range(100):
      print("account id: " + str(biggest100Influencers[i].id)
          + "; followers: " + str(biggest100Influencers[i].followers))
  
  
path = 'C:/Users/Matt/Documents/GitHub/Social-Network-Analysis/twitter_combined.txt'
main(path)