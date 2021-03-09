#r "C:\Program Files\workspacer\workspacer.Shared.dll"
#r "C:\Program Files\workspacer\plugins\workspacer.Bar\workspacer.Bar.dll"
#r "C:\Program Files\workspacer\plugins\workspacer.ActionMenu\workspacer.ActionMenu.dll"
#r "C:\Program Files\workspacer\plugins\workspacer.FocusIndicator\workspacer.FocusIndicator.dll"

using System;
using workspacer;
using workspacer.Bar;
using workspacer.ActionMenu;
using workspacer.FocusIndicator;

Action<IConfigContext> doConfig = (context) =>
{
    // Uncomment to switch update branch (or to disable updates)
    //context.Branch = Branch.None

    context.AddBar();
    context.AddFocusIndicator();
    var actionMenu = context.AddActionMenu();

    // Keybindings

    KeyModifiers mod = KeyModifiers.Alt;

    context.Keybinds.Unsubscribe(mod, Keys.Space);


    
    // WorkSpaces
    context.WorkspaceContainer.CreateWorkspaces("WEB", "OFFICE", "CHAT", "MUS");
};
return doConfig;
