import nuke

#############################################################################################################################################################################################
#############################################################                Disable in GUI knob            #################################################################################
#############################################################              Disable in Render knob           #################################################################################
#############################################################################################################################################################################################

def addKnob():
    n = nuke.thisNode()

    k = nuke.Tab_Knob('Disabling choices for rendering', 'Disable')
    n.addKnob(k)   

    l = nuke.Boolean_Knob('disableInRender','  Disable in Render     ')
    l.setTooltip('When "on", can disable this node while rendering')
    n.addKnob(l)

    m = nuke.Boolean_Knob('disableInGUI','  Disable in GUI')
    m.setTooltip('When "on", can disable this node while NUKE INTERFACE')
    m.setFlag(nuke.STARTLINE)         
    n.addKnob(m)

  
nuke.addOnUserCreate(addKnob)



#############################################################################################################################################################################################
################################################################             Autoswitch              ########################################################################################
#############################################################################################################################################################################################




def autoswitchknob():


    node = nuke.thisNode()
    knob = nuke.thisKnob()

    if knob.name() == "disableInRender":
        node["disableInGUI"].setValue(0)
    
        
    elif knob.name() == "disableInGUI":
        node["disableInRender"].setValue(0)
        
    
nuke.addKnobChanged(autoswitchknob)





#############################################################################################################################################################################################
################################################################             DISABLE IN GUI              ####################################################################################
#############################################################################################################################################################################################




def autoswitchgui():
    if nuke.thisNode().Class() != 'Viewer' :

        nuke.thisNode().knob('knobChanged').setValue('''
            
        
n = nuke.thisNode()

if n['disable'].value() != True or n['disable'].hasExpression():
    if n['disableInGUI'].value() == True:
        n['disable'].clearAnimated()  
        n['disable'].setExpression('$gui')
        
    else:
        n['disable'].setExpression('')
        n['disable'].clearAnimated()  
    
    
''')


nuke.addOnUserCreate(autoswitchgui)






#############################################################################################################################################################################################
################################################################             DISABLE IN RENDER              #################################################################################
#############################################################################################################################################################################################




##### before script #####
def before():
    allnodes = nuke.allNodes()
    a = []
    for node in nuke.allNodes():
        if node.knob("disableInGUI").value() == True:
            node['disable'].setExpression('')

###########################################################################################

    allnodes = nuke.allNodes()
    aa = []
    for node in nuke.allNodes():
        if node.knob("disableInRender").value() == True:
            node.knob("disable").setValue(True)
    
    
    for i in allnodes:
        if i.knob("disableInRender").getValue()==1.0:
            aa.append(i)
    print aa
    nodes= nuke.allNodes()
    result = "\n".join(["{}. {}".format(index, node.name()) for index, node in enumerate(aa, start=1)])
    if aa!=[]:
        nuke.message('Disabled nodes:\n'+result+ '\n\n')



    



##### before eachframerender script #####
def before_eachFrame():
    allnodes = nuke.allNodes()
    a = []
    for node in allnodes:
        if node.knob("disableInGUI").value() == True:
            node['disable'].setExpression('')

##########################################################################################

    allnodes = nuke.allNodes()
    aa = []
    for node in allnodes:
        if node.knob("disableInRender").value() == True:
            node.knob("disable").setValue(False)
            print 'Disabled node is "',node.name(), '\" '
        else:
            nonode = "no node is disabled"
            aa.append(nonode)
    print list(set(aa))

            
    


 

##### after eachframerender script #####
def after_eachFrame():
    allnodes = nuke.allNodes()
    a = []
    for node in allnodes:
        if node.knob("disableInGUI").value() == True:

            node['disable'].setExpression('')

##########################################################################################

    allnodes = nuke.allNodes()
    aa = []
    for node in allnodes:
        if node.knob("disableInRender").value() == True:
            node.knob("disable").setValue(True)
            print 'Disabled node is "',node.name(), '\" '
        else:
            nonode = "no node is disabled"
            aa.append(nonode)
    print list(set(aa))



##### after script #####
def after():
    allnodes = nuke.allNodes()
    a = []
    for node in nuke.allNodes():
        if node.knob("disableInGUI").value() == True:
            node['disable'].clearAnimated() 
            node['disable'].setExpression('$gui')

#######################################################################################

    allnodes = nuke.allNodes()
    aa = []
    for node in nuke.allNodes():
        if node.knob("disableInRender").value() == True:
            node.knob("disable").setValue(False)
    
    
    for i in allnodes:
        if i.knob("disableInRender").getValue()==1.0:
            aa.append(i)








nuke.addBeforeRender(before)
nuke.addAfterRender(after)
nuke.addBeforeFrameRender(before_eachFrame)
nuke.addAfterFrameRender(after_eachFrame)
