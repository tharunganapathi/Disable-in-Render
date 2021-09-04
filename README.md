With this script, 
    You can enable or disable the nodes while rendering and also
    You can enable or disable the nodes while in GUI
    
# Disable in Render
1. For every node in nuke you have a "Disable" tab.
2. There you can check "Disable in Render", at once you have enabled the checkbox, the respective node will not get rendered in output. (which is similar to aftereffects, but there it named as "Guide layer")
3. In addition to that, it will show you the popup of disabled nodes, before rendering.


![render_01](https://user-images.githubusercontent.com/65713157/132106801-a93a3921-7de5-4020-bc4c-be3b1be3aeeb.jpg)


# Disable in GUI
Once you have checked "Disable in GUI" in 'Disable' tab, the repective node will not show in the viewer. (similar to the process of $GUI)

I have made this for two reasons
1. This method, it will also works in normal GUI render. 
   But $GUI will not work in normal GUI render, it works only in background render and frame server render. 
2. When you use $GUI expression manually, it will create the keyframes, even after you have cleared that expression. 
