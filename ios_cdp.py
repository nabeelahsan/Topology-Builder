import namecheck

def parser (data, current_node, nodes, accessed, file_append):
		
	lines = data.splitlines()
	first_line = 0

	for y in range (0,len(lines)):
		if "Device ID" in lines[y]:
			first_line = y
			break

	nodes_file = open ('data/nodes-%s.txt' %file_append, 'a')
	links_file = open ('data/links-%s.txt' %file_append, 'a')

	lengths = []
	final1 = []
	unique = []
	cdp_nodes = []
	y = first_line + 1
	catos_check = True
	
	while y < len(lines):
		delimited_line = lines[y].split()
		final1 = delimited_line
		
		if "." in final1[0]:
			final1[0] = final1[0][0:(final1[0].index("."))]
			catos_check = False
			
		if ("(" or ")") in final1[0]:
			final1[0] = final1[0][(final1[0].index('('))+1:(final1[0].index(')'))]	
		
		if len(delimited_line) == 1:
			
			final1 = final1 + lines[y+1].split()
			y+=1
		
		if catos_check is False:
			final2 = final1[:3] + final1[-2:]		
			final3 = current_node + "\t" + final2[0].lower() + "\t" + final2[1] + final2[2] + "\t" + final2[3] + final2[4] + "\n"
		else:
			final2 = final1[:3] + final1[-1:]		
			final3 = current_node + "\t" + final2[0].lower() + "\t" + final2[1] + final2[2] + "\t" + final2[3] + "\n"

		if namecheck.namecheck(str(final2[0].lower())) is False:
			y+=1
			catos_check = True
			continue
		
		if (final2[0].lower() != current_node.lower()) and (final2[0].lower() not in cdp_nodes):
			cdp_nodes.append (final2[0].lower())

		if (final2[0].lower() != current_node.lower()) and (final2[0].lower() not in nodes):
			unique.append (final2[0].lower())		
			nodes.append (final2[0].lower())		
					
		if (final2[0].lower() not in accessed):
			links_file.write(final3)
		
		y+=1
		catos_check = True
	
	return cdp_nodes, unique