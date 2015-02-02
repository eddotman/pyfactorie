from subprocess import check_output
from re import escape
from utilities import Node

class FactorieParser(object):
  def __init__(self):
    pass

  def parse_sentence(self, sentence, port=3228):
    #Requires parsing server to be running!
    #Break raw parser output into nested lists
    sentence = escape(sentence.encode('cp1252'))
    sentence_str = str(check_output(['echo ' + str(sentence) + ' | nc localhost ' + str(port)], shell=True).encode('utf8'))
    sentence_list = sentence_str.split('\n\n')
    sentence_list = [s.split('\n') for s in sentence_list]
    word_data = []
    for sentence in sentence_list:
      if len(sentence) > 1:
        word_data.append([])
        for word in sentence:
          word_data[-1].append(word.split('\t'))

    #Store in unlinked nodes
    nodes = []
    for sentence in word_data:
      node_list = []
      for line in sentence:
        if len(line) > 1: #Parser generates some blank lines
          name = str(line[2])
          node = Node(name, [])
          node.data = {
            'id': int(line[0]),
            'sent_id': int(line[1]),
            'pos': str(line[4]),
            'parent_id': int(line[5]),
            'phrase': str(line[6])
          }
          node_list.append(node)
      nodes.append(node_list)

    #Link nodes into a tree
    for sentence_tree in nodes:
      for node in sentence_tree:
        parent_node = [n for n in sentence_tree if n.data['sent_id'] == node.data['parent_id']]
        if len(parent_node) == 1:
          parent_node[0].add_child(node)

    #Find roots
    roots = []
    for tree in nodes:
      for node in tree:
        if node.data['parent_id'] == 0:
          roots.append(node)

    return roots
