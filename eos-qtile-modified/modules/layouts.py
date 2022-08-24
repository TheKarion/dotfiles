from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Bsp(margin=0, border_focus='#5294e2'),
    layout.MonadTall(margin=0, border_focus='#5294e2',
                     border_normal='#2c5380'),
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(margin=0, border_focus='#5294e2'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(border_focus='#5294e2'),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(border_focus='#5294e2'),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title="Origin"), # EA Origin Fix
])
