class Node(object):
  def __init__(self, name, children):
    self.data = {}
    self.name = name
    self.children = children

  def __str__(self):
    return self.name

  def add_child(self, child):
    self.children.append(child)


class NodeHandler(object):
  def __init__(self):
    self.reset()

  def reset(self):
    self.found_node = None
    self.found_nodes = []

  def find_node_by_id(self, node, target_id):
    if int(node.data['id']) == int(target_id):
      self.found_node = node
    else:
      for child in node.children:
        self.find_node_by_id(child, target_id)

  def find_all_by_name(self, node, target_name):
    if node.name == target_name and node not in self.found_nodes:
      self.found_nodes.append(node)
    else:
      for child in node.children:
        self.find_all_by_name(child, target_name)

  def find_all_by_prop_val(self, node, prop, value):
    if node.data[prop] == value and node not in self.found_nodes:
      self.found_nodes.append(node)

    for child in node.children:
      self.find_all_by_prop_val(child, prop, value)

  def find_all_children(self, node):
    self.found_nodes.append(node)

    for child in node.children:
      self.find_all_children(child)
