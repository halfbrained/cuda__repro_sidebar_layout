import os
from cudatext import *

fn_icon = os.path.join(os.path.dirname(__file__), 'terminal.png')

class Command:
    def __init__(self):
        self.h_dlg = None
    
    def open_init(self):

        self.h_dlg = self.init_form()
        
        app_proc(PROC_BOTTOMPANEL_ADD_DIALOG, ('Fake', self.h_dlg, fn_icon))


    def init_form(self):
        h = dlg_proc(0, DLG_CREATE)
        dlg_proc(h, DLG_PROP_SET, prop={
            'border': False,
            })


        # parent panels 
        n = dlg_proc(h, DLG_CTL_ADD, 'panel')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'name': 'panels_parent',
            'a_l': ('', '['),
            'a_t': ('', '['),
            'a_r': ('', ']'),
            'a_b': ('', ']'),
            'cap': '',
            'color': 0xff,
            })
        h_panels_parent = dlg_proc(h, DLG_CTL_HANDLE, index=n)
        
        n = dlg_proc(h, DLG_CTL_ADD, 'panel')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'p': 'panels_parent',
            'name': 'statusb_parent',
            #'a_l': ('', '['),
            #'a_t': None,
            #'a_r': ('', ']'),
            #'a_b': ('', ']'),
            'align': ALIGN_RIGHT,
            #'w': 150,
            'cap': 'statusbar',
            'color': 0xff00, # green
            })
        h_statusb_parent = dlg_proc(h, DLG_CTL_HANDLE, index=n)
        

        n = dlg_proc(h, DLG_CTL_ADD, 'panel')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'p': 'panels_parent',
            'name': 'input_parent',
            #'a_l': ('', '['),
            #'a_t': None,
            #'a_r': ('', ']'),
            #'a_b': ('', ']'),
            'align': ALIGN_CLIENT,
            'cap': 'inputs',
            'color': 0xff0000, # blue
            }) 
        h_input_parent = dlg_proc(h, DLG_CTL_HANDLE, index=n)


        # widgets RIGHT GREEEN
        #### btn works
        use_btn = False # or statusbar
        if use_btn:
            n = dlg_proc(h, DLG_CTL_ADD, 'button_ex')
            dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
                'p': 'statusb_parent',
                'name': 'btn',
                'sp_a': 10,
                'cap': 'Breaks Many Braks Looong',
                'hint': 'Hotkey: Break',
                'align': ALIGN_CLIENT,
                })
        #### statusbar - error
        else: 
            n = dlg_proc(h, DLG_CTL_ADD, 'statusbar')
            dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
                'p': 'statusb_parent',
                'name': 'sb',
                'w': 90,
                'h': 40,
                'sp_a': 10,
                'cap': 'Breaks Many Braks LKonk',
                'hint': 'Hotkey: Break',
                'align': ALIGN_CLIENT,
                })
        

        # widgets LEFT BLUE
        n = dlg_proc(h, DLG_CTL_ADD, 'button_ex')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'p': 'input_parent',
            'name': 'break',
            'w': 90,
            #'h': 40,
            'cap': 'Break',
            'hint': 'Hotkey: Break',
            'sp_a': 10,
            'align': ALIGN_RIGHT,
            })

        n = dlg_proc(h, DLG_CTL_ADD, 'editor_combo')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'p': 'input_parent',
            'name': 'input',
            'border': True,
            #'h': 40,
            'sp_a': 10,
            'align': ALIGN_CLIENT,
            'texthint': 'Enter command here',
            })

        return h
        
    def open(self):
        if not self.h_dlg:
            self.open_init()
            

        