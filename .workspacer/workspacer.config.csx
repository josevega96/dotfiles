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

    //Workspace apps
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Edge") ? context.WorkspaceContainer["WEB"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Word") ? context.WorkspaceContainer["OFFICE"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Powerpoint") ? context.WorkspaceContainer["OFFICE"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Excel") ? context.WorkspaceContainer["OFFICE"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Flie Explorer") ? context.WorkspaceContainer["OFFICE"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("VSCodium") ? context.WorkspaceContainer["OFFICE"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("WhatsApp") ? context.WorkspaceContainer["CHAT"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Telegram") ? context.WorkspaceContainer["CHAT"] : null);
    context.WindowRouter.AddRoute((window) => window.Title.Contains("Spotify") ? context.WorkspaceContainer["MUS"] : null);
     

    //Custom Rules
    context.WindowRouter.AddFilter((window) => !window.Title.Contains("Search"));
    context.WindowRouter.AddFilter((window) => !window.Title.Contains("PowerLauncher"));
};
return doConfig;
