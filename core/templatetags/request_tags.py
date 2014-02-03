from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def change_request(context):
    aa = context['posts'].object_list.model.objects.all()
    #node = context['block'].
    	
    #import pdb; pdb.set_trace()
    return context['request'].META['REMOTE_ADDR']




@register.simple_tag(takes_context=True)
def change_http(context):
    node = context['block'].nodelist
    print len(node)
    #abc = []
    #for a in node:
    #    import pdb; pdb.set_trace()
	# you have to use try except here because some of the node list is not having any string variable
    #	try:
    #       if str(a.s).__contains__('src'):
    #		import pdb; pdb.set_trace()
    #            print str(a.s)
                #aa = str(a.s).replace('http', 'https')
		#abc.append(aa) 
    #            return str(a.s).replace('http', 'https')
    #   except AttributeError:
    #        import pdb; pdb.set_trace()
            #abc.append(a)
    #           return a
 
    #    else:
    #        import pdb; pdb.set_trace()
    #        print str(a.s)
            #abc.append(a)
    #        return a

    return "hello" 



class Change(template.Node):
    
    def __init__(self, nodelist):
        self.nodelist = nodelist
       
    def render(self, context):
        import pdb; pdb.set_trace()
        code = self.nodelist.render(context)
        # here should be logic for the a tag also so that we can change the also the hyperlink 
        codeval = str(code).replace('src="http:', 'src="https:').decode('unicode_escape')       
        return codeval


@register.tag(name='http_to_https')
def change_http_to_https(parser, token):
    nodelist = parser.parse(('endhttp_to_https',))
    parser.delete_first_token()
    return Change(nodelist)
