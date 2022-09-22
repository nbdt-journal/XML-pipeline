    import networkx as nx 

    import node
    from node import Node 
    from element import Element 

    ''' Building a graph for verse-line ''' 
    # Defining Elements
    verse_line = Element('verse-line')
    G_verse_line = nx.DiGraph()
    first_node = node.get_first_node()
    last_node = node.get_last_node()
    G_verse_line.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node, fn_node, target_node, xref_node])
    
    
    for i in list(G_verse_line.nodes):
        for j in list(G_verse_line.nodes):
            if i.element.name != 'last':
                if j.element.name != 'first':
                    G_verse_line.add_edge(i, j)
    # Creating the Nodes
    verse_line_node = Node(element=verse_line, graph=G_verse_line)