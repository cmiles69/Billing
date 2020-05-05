#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=XvnVAjvfKOM&t=352s  # Part 1
# https://www.youtube.com/watch?v=rTpnyb3y5-w         # Part 2
# https://www.youtube.com/watch?v=aVIpje43mPk         # Part 3
# From Web code -> Rangesh ?
#
# Part 1
# 4:38, 6:00, 6:55, 7:38, 8:34, 11:50 
# 16:00, 18:37, 27:59, 29:31, 32:33, 34:05
#
# Part 2 -> 8:08, 10:32, 13:56, 15:40, 18:08, 19:51
# 22:45, 23:17, 26:06, 29:21, 32:47, 33:24, 34:46,
# 35:39, 37:01, 40:17, 43:23, 44:10, 45:44, 49:49
#
# part 3 -> 00:55

# Craig Miles -> cmiles69@hushmail.com
# https://github.com/cmiles69/Billing.git

import tkinter
import tkinter.scrolledtext as tkst
import tkinter.messagebox
import os
import sys
import tempfile
import subprocess
import random
import names    # -> You will need to pip install this module.
import secrets  # -> And also this module.
from tkinter import font

class Billing_Class( object ):

    def __init__( self, root ):
        self.root = root
        self.initUI()

    def initUI( self ):
        self.root.title( 'Billing Software' )
        self.geometry = self.screen_size( size = 0.75 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.root.protocol( 'WM_DELETE_WINDOW', self.ask_quit )
        self.center_root()
        self.root.configure( background = 'deep sky blue' )
        self.create_fonts()
        self.create_variables()
        self.create_frames()

    def screen_size( self, size ):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return( '{}x{}+{}+{}' 
        .format( int( width ), int( height ), 0, 0 ))

    def center_root( self ):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
        int( self.root.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.root.winfo_screenheight() // 2 - window_height // 2 )
        self.root.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))

#========================Create Fonts===================================        

    def create_fonts( self ):
        self.title_font = font.Font( family = 'LuxiSerif',
                                     size = 30,
                                     weight = 'normal' )
        self.label_font = font.Font( family = 'LuxiSerif',
                                     size = 15,
                                     weight = 'normal' )
        self.entry_font = font.Font( family = 'DejaVu Serif',
                                     size = 15,
                                     weight = 'normal' )
        self.label_frame_font = font.Font( family = 'Suruma',
                                           size = 15,
                                           weight = 'normal' )
        self.btn_font = font.Font( family = 'Bitstream Charter',
                                   size = 16,
                                   weight = 'bold' )

#========================Create Variables===============================

    def create_variables( self ):
        self.customer_name              = tkinter.StringVar()
        self.contact_number             = tkinter.StringVar()
        self.bill_number                = tkinter.StringVar()
        self.bath_soap                  = tkinter.IntVar()
        self.face_cream                 = tkinter.IntVar()
        self.face_wash                  = tkinter.IntVar()
        self.hair_spray                 = tkinter.IntVar()
        self.hair_gel                   = tkinter.IntVar()
        self.body_lotion                = tkinter.IntVar()
        self.rice                       = tkinter.IntVar()
        self.food_oil                   = tkinter.IntVar()
        self.red_lentil                 = tkinter.IntVar()
        self.wheat                      = tkinter.IntVar()
        self.sugar                      = tkinter.IntVar()
        self.tea                        = tkinter.IntVar()
        self.maaza                      = tkinter.IntVar()
        self.coke                       = tkinter.IntVar()
        self.frooti                     = tkinter.IntVar()
        self.thums_up                   = tkinter.IntVar()
        self.limca                      = tkinter.IntVar()
        self.sprite                     = tkinter.IntVar()
        self.total_cosmetic_price       = tkinter.StringVar()
        self.total_grocery_price        = tkinter.StringVar()
        self.total_cold_drinks_price    = tkinter.StringVar()
        self.cosmetic_tax               = tkinter.StringVar()
        self.grocery_tax                = tkinter.StringVar()
        self.cold_drinks_tax            = tkinter.StringVar()

#========================Create Frames==================================                                     

    def create_frames( self ):
        self.create_title_bar()
        self.create_customer_details()
        self.create_cosmetics_frame()
        self.create_grocery_frame()
        self.create_cold_drinks()
        self.create_reciept()
        self.create_billing_menu()
        self.create_buttons()

#========================Create Title Bar===============================

    def create_title_bar( self ):
        self.lbl_title_bar = tkinter.Label( self.root,
                                borderwidth  = 10,
                                background = '#074463',
                                foreground = 'gold',
                                font = self.title_font,
                                text = 'Billing Software',
                                relief = tkinter.GROOVE )
        self.lbl_title_bar.place( relx = 0,
                                  rely = 0,
                                  relwidth = 1,
                                  relheight = 0.1 )

#========================Create Customer Details========================

    def create_customer_details( self ):
        self.lblfrm_customer = tkinter.LabelFrame( self.root,
                                font = self.label_frame_font,
                                borderwidth = 10,
                                text = 'Customer Details',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lblfrm_customer.place( relx = 0,
                                    rely = 0.1,
                                    relwidth = 1,
                                    relheight = 0.11 )

        self.lbl_customer_name = tkinter.Label( self.lblfrm_customer,
                                font = self.label_font,
                                text = 'Customer Name :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_customer_name.place( relx = 0.005,
                                      rely = 0.05 )
        self.ent_customer_name = tkinter.Entry( self.lblfrm_customer,
                                borderwidth = 5,
                                textvariable = self.customer_name,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_customer_name.place( relx = 0.145,
                                      rely = 0,
                                      relwidth = 0.17 )

        self.lbl_contact_number = tkinter.Label( self.lblfrm_customer,
                                font = self.label_font,
                                text = 'Contact No. :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_contact_number.place( relx = 0.33,
                                       rely = 0.05 )
        self.ent_contact_number = tkinter.Entry( self.lblfrm_customer,
                                borderwidth = 5,
                                textvariable = self.contact_number,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_contact_number.place( relx = 0.44,
                                       rely = 0,
                                       relwidth = 0.13 )

        self.lbl_bill_number = tkinter.Label( self.lblfrm_customer,
                                font = self.label_font,
                                text = 'Bill No. :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_bill_number.place( relx = 0.584,
                                    rely = 0.05 )
        self.ent_bill_number = tkinter.Entry( self.lblfrm_customer,
                                borderwidth = 5,
                                textvariable = self.bill_number,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_bill_number.place( relx = 0.660,
                                    rely = 0,
                                    relwidth = 0.13 )

        self.btn_search = tkinter.Button( self.lblfrm_customer,
                                borderwidth = 3,
                                pady = 1,
                                background = '#074463',
                                activeforeground = 'gold',
                                activebackground = 'blue',
                                font = self.btn_font,
                                text = 'Search' )       
        self.btn_search.place( relx = 0.825,
                               rely = 0,
                               relwidth = 0.13 )

#===================Create Cosmetics Frame==============================

    def create_cosmetics_frame( self ):
        self.lblfrm_cosmetics = tkinter.LabelFrame( self.root,
                                font = self.label_frame_font,
                                borderwidth = 10,
                                text = 'Cosmetics',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lblfrm_cosmetics.place( relx = 0,
                                     rely = 0.210,
                                     relwidth = 0.25,
                                     relheight = 0.50 )

        self.lbl_bath_soap = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Bath Soap :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_bath_soap.place( relx = 0.02,
                                  rely = 0.05 )
        self.ent_bath_soap = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.bath_soap,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_bath_soap.place( relx = 0.5,
                                  rely = 0.04,
                                  relwidth = 0.47 )

        self.lbl_face_cream = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Face Cream :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_face_cream.place( relx = 0.02,
                                   rely = 0.19 )
        self.ent_face_cream = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.face_cream,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_face_cream.place( relx = 0.5,
                                   rely = 0.18,
                                   relwidth = 0.47 )

        self.lbl_face_wash = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Face Wash :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_face_wash.place( relx = 0.02,
                                  rely = 0.33 )
        self.ent_face_wash = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.face_wash,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_face_wash.place( relx = 0.5,
                                  rely = 0.32,
                                  relwidth = 0.47 )

        self.lbl_hair_spray = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Hair Spray :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_hair_spray.place( relx = 0.02,
                                   rely = 0.47 )
        self.ent_hair_spray = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.hair_spray,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_hair_spray.place( relx = 0.5,
                                   rely = 0.46,
                                   relwidth = 0.47 )

        self.lbl_hair_gel = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Hair Gel :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_hair_gel.place( relx = 0.02,
                                 rely = 0.61 )
        self.ent_hair_gel = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.hair_gel,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_hair_gel.place( relx = 0.5,
                                 rely = 0.60,
                                 relwidth = 0.47 )

        self.lbl_body_lotion = tkinter.Label( self.lblfrm_cosmetics,
                                font = self.label_font,
                                text = 'Body Lotion :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_body_lotion.place( relx = 0.02,
                                    rely = 0.75 )
        self.ent_body_lotion = tkinter.Entry( self.lblfrm_cosmetics,
                                borderwidth = 5,
                                textvariable = self.body_lotion,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_body_lotion.place( relx = 0.5,
                                    rely = 0.74,
                                    relwidth = 0.47 )

#=======================Create Grocery Frame============================

    def create_grocery_frame( self ):
        self.lblfrm_grocery = tkinter.LabelFrame( self.root,
                                font = self.label_frame_font,
                                borderwidth = 10,
                                text = 'Grocery',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lblfrm_grocery.place( relx = 0.255,
                                   rely = 0.210,
                                   relwidth = 0.25,
                                   relheight = 0.50 )

        self.lbl_rice = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Rice :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_rice.place( relx = 0.02,
                             rely = 0.05 )
        self.ent_rice = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.rice,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_rice.place( relx = 0.5,
                             rely = 0.04,
                             relwidth = 0.47 )

        self.lbl_food_oil = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Food Oil :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_food_oil.place( relx = 0.02,
                                 rely = 0.19 )
        self.ent_food_oil = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.food_oil,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_food_oil.place( relx = 0.5,
                                 rely = 0.18,
                                 relwidth = 0.47 )

        self.lbl_red_lentil = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Red_Lentil :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_red_lentil.place( relx = 0.02,
                                   rely = 0.33 )
        self.ent_red_lentil = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.red_lentil,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_red_lentil.place( relx = 0.5,
                                   rely = 0.32,
                                   relwidth = 0.47 )

        self.lbl_wheat = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Wheat :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_wheat.place( relx = 0.02,
                              rely = 0.47 )
        self.ent_wheat = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.wheat,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_wheat.place( relx = 0.5,
                              rely = 0.46,
                              relwidth = 0.47 )

        self.lbl_sugar = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Sugar :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_sugar.place( relx = 0.02,
                              rely = 0.61 )
        self.ent_sugar = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.sugar,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_sugar.place( relx = 0.5,
                              rely = 0.60,
                              relwidth = 0.47 )

        self.lbl_tea = tkinter.Label( self.lblfrm_grocery,
                                font = self.label_font,
                                text = 'Tea :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_tea.place( relx = 0.02,
                            rely = 0.75 )
        self.ent_tea = tkinter.Entry( self.lblfrm_grocery,
                                borderwidth = 5,
                                textvariable = self.tea,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_tea.place( relx = 0.5,
                            rely = 0.74,
                            relwidth = 0.47 )

#======================Create Cold Drinks===============================

    def create_cold_drinks( self ):
        self.lblfrm_cold_drinks = tkinter.LabelFrame( self.root,
                                font = self.label_frame_font,
                                borderwidth = 10,
                                text = 'Cold Drinks',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lblfrm_cold_drinks.place( relx = 0.51,
                                       rely = 0.210,
                                       relwidth = 0.25,
                                       relheight = 0.50 )

        self.lbl_maaza = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Maaza :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_maaza.place( relx = 0.02,
                              rely = 0.05 )
        self.ent_maaza = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.maaza,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_maaza.place( relx = 0.5,
                              rely = 0.04,
                              relwidth = 0.47 )

        self.lbl_coke = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Coke :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_coke.place( relx = 0.02,
                             rely = 0.19 )
        self.ent_coke = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.coke,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_coke.place( relx = 0.5,
                             rely = 0.18,
                             relwidth = 0.47 )

        self.lbl_frooti = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Frooti :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_frooti.place( relx = 0.02,
                               rely = 0.33 )
        self.ent_frooti = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.frooti,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_frooti.place( relx = 0.5,
                               rely = 0.32,
                               relwidth = 0.47 )

        self.lbl_thums_up = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Thums Up :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_thums_up.place( relx = 0.02,
                                 rely = 0.47 )
        self.ent_thums_up = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.thums_up,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_thums_up.place( relx = 0.5,
                                 rely = 0.46,
                                 relwidth = 0.47 )

        self.lbl_limca = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Limca :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_limca.place( relx = 0.02,
                              rely = 0.61 )
        self.ent_limca = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.limca,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_limca.place( relx = 0.5,
                              rely = 0.60,
                              relwidth = 0.47 )

        self.lbl_sprite = tkinter.Label( self.lblfrm_cold_drinks,
                                font = self.label_font,
                                text = 'Sprite :',
                                background = '#074463',
                                foreground = 'ghost white' )
        self.lbl_sprite.place( relx = 0.02,
                               rely = 0.75 )
        self.ent_sprite = tkinter.Entry( self.lblfrm_cold_drinks,
                                borderwidth = 5,
                                textvariable = self.sprite,
                                font = self.entry_font,
                                background = 'green',
                                foreground = 'gold' )
        self.ent_sprite.place( relx = 0.5,
                               rely = 0.74,
                               relwidth = 0.47 )

#=========================Create Reciept================================

    def create_reciept( self ):
        self.reciept = tkst.ScrolledText( self.root,
                                          borderwidth = 5,
                                          background = 'cyan',
                                          relief = tkinter.GROOVE )
        self.reciept.place( relx = 0.76,
                            rely = 0.210,
                            relwidth = 0.24,
                            relheight = 0.50 )
        self.lbl_reciept = tkinter.Label( self.reciept,
                                font = self.label_font,
                                text = 'Reciept Area',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lbl_reciept.place( relx = 0,
                                rely = 0,
                                relwidth = 1 )
        self.reciept_header() 

#============================Create Billing Menu========================

    def create_billing_menu( self ):
        self.lblfrm_billing_menu = tkinter.LabelFrame( self.root,
                                font = self.label_frame_font,
                                borderwidth = 10,
                                text = 'Billing Menu',
                                background = '#074463',
                                foreground = 'gold',
                                relief = tkinter.GROOVE )
        self.lblfrm_billing_menu.place( relx = 0,
                                        rely = 0.72,
                                        relwidth = 1,
                                        relheight = 0.28 )

        self.lbl_total_cosmetic_price = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Total Cosmetic Price :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_total_cosmetic_price.place( relx = 0.02,
                                             rely = 0.05 )
        self.ent_total_cosmetic_price = tkinter.Entry(
                            self.lblfrm_billing_menu,
                            borderwidth = 5,
                            textvariable = self.total_cosmetic_price,
                            font = self.entry_font,
                            background = 'green',
                            foreground = 'gold' )
        self.ent_total_cosmetic_price.place( relx = 0.21,
                                             rely = 0.04,
                                             relwidth = 0.11 )

        self.lbl_total_grocery_price = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Total Grocery Price :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_total_grocery_price.place( relx = 0.02,
                                            rely = 0.33 )
        self.ent_total_grocery_price = tkinter.Entry(
                            self.lblfrm_billing_menu,
                            borderwidth = 5,
                            textvariable = self.total_grocery_price,
                            font = self.entry_font,
                            background = 'green',
                            foreground = 'gold' )
        self.ent_total_grocery_price.place( relx = 0.21,
                                            rely = 0.32,
                                            relwidth = 0.11 )

        self.lbl_total_cold_drinks_price = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Total Cold Drinks Price :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_total_cold_drinks_price.place( relx = 0.02,
                                                rely = 0.62 )
        self.ent_total_cold_drinks_price = tkinter.Entry(
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        textvariable = self.total_cold_drinks_price,
                        font = self.entry_font,
                        background = 'green',
                        foreground = 'gold' )
        self.ent_total_cold_drinks_price.place( relx = 0.21,
                                                rely = 0.61,
                                                relwidth = 0.11 )

        self.lbl_cosmetic_tax = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Cosmetic Tax :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_cosmetic_tax.place( relx = 0.34,
                                     rely = 0.05 )
        self.ent_cosmetic_tax = tkinter.Entry(
                            self.lblfrm_billing_menu,
                            borderwidth = 5,
                            textvariable = self.cosmetic_tax,
                            font = self.entry_font,
                            background = 'green',
                            foreground = 'gold' )
        self.ent_cosmetic_tax.place( relx = 0.48,
                                     rely = 0.04,
                                     relwidth = 0.11 )

        self.lbl_grocery_tax = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Grocery Tax :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_grocery_tax.place( relx = 0.34,
                                    rely = 0.33 )
        self.ent_grocery_tax = tkinter.Entry(
                            self.lblfrm_billing_menu,
                            borderwidth = 5,
                            textvariable = self.grocery_tax,
                            font = self.entry_font,
                            background = 'green',
                            foreground = 'gold' )
        self.ent_grocery_tax.place( relx = 0.48,
                                    rely = 0.32,
                                    relwidth = 0.11 )

        self.lbl_cold_drinks_tax = tkinter.Label( 
                                    self.lblfrm_billing_menu,
                                    font = self.label_font,
                                    text = 'Cold Drinks Tax :',
                                    background = '#074463',
                                    foreground = 'ghost white' )
        self.lbl_cold_drinks_tax.place( relx = 0.34,
                                        rely = 0.62 )
        self.ent_cold_drinks_tax = tkinter.Entry(
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        textvariable = self.cold_drinks_tax,
                        font = self.entry_font,
                        background = 'green',
                        foreground = 'gold' )
        self.ent_cold_drinks_tax.place( relx = 0.48,
                                        rely = 0.61,
                                        relwidth = 0.11 )

#=======================Button Callbacks================================

    def ask_quit( self ):
        exit_program = tkinter.messagebox.askyesno(
            title = 'Billing Software System',
            message = 'Confirm if you want to exit program?' )
        if exit_program > 0:
            self.root.destroy()
        else:
            return( None )

    def save_reciept( self ):
        SR = tkinter.messagebox.askyesno(
            title = 'Save The Reciept To File',
            message = 'Do You Want To Save The Reciept?' )
        if SR > 0:
            self.data_reciept = self.reciept.get( 1.0, tkinter.END )
            tmp = open( str( self.bill_number.get()) + '.txt', 'w' )
            tmp.write( self.data_reciept )
            tmp.close()
        else:
            return( None )

    def print_reciept( self ):
        tmp = self.reciept.get( 1.0, 'end-1c' )
        tmp_file = tempfile.mktemp( '.txt' )
        open( tmp_file, 'w' ).write( tmp )
        if sys.platform.startswith( 'win' ):
            os.startfile( tmp_file, 'print' )
        else:
            if sys.platform == 'linux':
                with open( tmp_file ) as f:
                    # call the system's lpr command
                    p = subprocess.Popen(["lpr"], stdin=f, shell=True)  
                    output = p.communicate()[0]

    def clear_values( self ):
        self.customer_name.set( '' )          
        self.contact_number.set( '' )         
        self.bill_number.set( '' )            
        self.bath_soap.set( '' )              
        self.face_cream.set( '' )             
        self.face_wash.set( '' )              
        self.hair_spray.set( '' )             
        self.hair_gel.set( '' )               
        self.body_lotion.set( '' )            
        self.rice.set( '' )                   
        self.food_oil.set( '' )               
        self.red_lentil.set( '' )             
        self.wheat.set( '' )                  
        self.sugar.set( '' )                  
        self.tea.set( '' )                    
        self.maaza.set( '' )                  
        self.coke.set( '' )                   
        self.frooti.set( '' )                 
        self.thums_up.set( '' )               
        self.limca.set( '' )                  
        self.sprite.set( '' )                 
        self.total_cosmetic_price.set( '' )   
        self.total_grocery_price.set( '' )    
        self.total_cold_drinks_price.set( '' )
        self.cosmetic_tax.set( '' )           
        self.grocery_tax.set( '' )            
        self.cold_drinks_tax.set( '' )
        self.reciept.delete( 1.0, tkinter.END )
        self.reciept_header()        

    def total_prices( self ):
        #===============Total Cosmetic Price=================
        self.BS = self.bath_soap.get()   * 4.0
        self.FC = self.face_cream.get()  * 12.0
        self.FW = self.face_wash.get()   * 6.0
        self.HS = self.hair_spray.get()  * 18.0
        self.HG = self.hair_gel.get()    * 14.0
        self.BL = self.body_lotion.get() * 18.0
        self.TCP = float( self.BS  +
                          self.FC  +
                          self.FW  +
                          self.HS  +
                          self.HG  +
                          self.BL )
        string_TCP = '$' + str( self.TCP ) 
        self.total_cosmetic_price.set( string_TCP )
        #===============Cosmetic Tax=========================
        self.CT = round( self.TCP * 0.05 )
        string_CT = '$' + str( self.CT )
        self.cosmetic_tax.set( string_CT )
        #===============Total Grocery Price==================
        self.RI = self.rice.get()         * 8.0
        self.FO = self.food_oil.get()     * 18.0
        self.RL = self.red_lentil.get()   * 6.0
        self.WH = self.wheat.get()        * 24.0
        self.SG = self.sugar.get()        * 4.5
        self.TE = self.tea.get()          * 1.50

        self.TGP = float( self.RI +
                          self.FO +
                          self.RL +
                          self.WH +
                          self.SG +
                          self.TE )
        string_TGP = '$' + str( self.TGP )
        self.total_grocery_price.set( string_TGP )
        #===============Grocery Tax==========================
        self.GT = round( self.TGP * 0.10 )
        string_GT = '$' + str( self.GT )
        self.grocery_tax.set( string_GT )
        #===============Total Cold Drinks Price==============
        self.MA = self.maaza.get()     * 6.0
        self.CO = self.coke.get()      * 6.0
        self.FR = self.frooti.get()    * 5.0
        self.TH = self.thums_up.get()  * 4.5
        self.LI = self.limca.get()     * 4.0
        self.SP = self.sprite.get()    * 6.0
        self.TDP = float(self.MA + 
                         self.CO + 
                         self.FR +
                         self.TH +
                         self.LI +
                         self.SP  )
        string_TDP = '$' + str( self.TDP )
        self.total_cold_drinks_price.set( string_TDP )
        #===============Cold Drinks Tax======================
        self.CDT = round( self.TDP * 0.05 )
        string_CDT = '$' + str( self.CDT )
        self.cold_drinks_tax.set( string_CDT )
        #================Sub Total===========================
        self.sub_total = float(( self.TCP + self.TGP + self.TDP ))
        self.tax_total = float(( self.CT  + self.GT  + self.CDT ))
        #================Total Owed==========================
        self.owed_total = float(( self.sub_total + self.tax_total ))

    def reciept_header( self ):
        self.reciept.insert( tkinter.END, '\n\n' ) # Get past label
        self.reciept.insert( tkinter.END,
                            '      Welcome To Billing Software' )  #6
        self.reciept.insert( tkinter.END, '\n\n' ) # Some Space.

    def generate_reciept( self ):
        self.reciept.delete( 1.0, tkinter.END )
        self.reciept_header()
        self.reciept.insert( tkinter.END, 
            f'\nBill Number :   { self.bill_number.get()}')
        self.reciept.insert( tkinter.END,
            f'\nCustomer Name : { self.customer_name.get()}')
        self.reciept.insert( tkinter.END,
            f'\nPhone Number :  { self.contact_number.get()}')

        self.reciept.insert( tkinter.END,
            f'\n=======================================')
        self.reciept.insert( tkinter.END,
            f'\n Products:         Qty:          Price:' )  # 9, 10
        self.reciept.insert( tkinter.END,
            f'\n=======================================')

#=====================Cosmetics=========================================      

        if self.bath_soap.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Bath Soap         {self.bath_soap.get()}\
            {self.BS}') # 9,13
        if self.face_cream.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Face Cream        {self.face_cream.get()}\
            {self.FC}')  #8,13
        if self.face_wash.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Face Wash         {self.face_wash.get()}\
            {self.FW}')  #9,11
        if self.hair_spray.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Hair Spray        {self.hair_spray.get()}\
            {self.HS}')  #8,12
        if self.hair_gel.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Hair Gel          {self.hair_gel.get()}\
            {self.HG}')  #10,12
        if self.body_lotion.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Body Lotion       {self.body_lotion.get()}\
            {self.BL}') #7,12

#========================Grocery========================================

        if self.rice.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Rice\t\t   {self.rice.get()}\t\t{self.RI}')
        if self.food_oil.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Food Oil          {self.food_oil.get()}\
            {self.FO}')
        if self.red_lentil.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Red Lentil        {self.red_lentil.get()}\
            {self.RL}')
        if self.wheat.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Wheat\t\t   {self.wheat.get()}\t\t{self.WH}')
        if self.sugar.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Sugar\t\t   {self.sugar.get()}\t\t{self.SG}')
        if self.tea.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Tea\t\t   {self.tea.get()}\t\t{self.TE}')

#=========================Cold Drinks===================================
    
        if self.maaza.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Mazza\t\t   {self.maaza.get()}\t\t{self.MA}')
        if self.coke.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Coke\t\t   {self.coke.get()}\t\t{self.CO}')
        if self.frooti.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Frooti\t\t   {self.frooti.get()}\t\t{self.FR}')
        if self.thums_up.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Thums Up          {self.thums_up.get()}\
            {self.TH}')
        if self.limca.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Limca\t\t   {self.limca.get()}\t\t{self.LI}')
        if self.sprite.get() != 0:
            self.reciept.insert( tkinter.END,
            f'\n Sprite\t\t   {self.sprite.get()}\t\t{self.SP}')

#===========================Totals & Tax============================

        self.reciept.insert( tkinter.END,
            f'\n=======================================')
        self.reciept.insert( tkinter.END,
            f'\n Sub Total Amount:              {self.sub_total:.2f}' )
        self.reciept.insert( tkinter.END,
            f'\n Taxation:                      {self.tax_total:.2f}' )
        self.reciept.insert( tkinter.END,
            f'\n Total Owed:                    {self.owed_total:.2f}' )
        self.reciept.insert( tkinter.END,
            f'\n=======================================')

        self.save_reciept()

#===========================Create Buttons==============================

    def create_buttons( self ):
        self.btn_total = tkinter.Button( 
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        background = 'purple1',
                        foreground = 'gold',
                        activeforeground = 'gold',
                        activebackground = 'royal blue',
                        font = self.btn_font,
                        text = 'Total',
                        command =  self.total_prices )
        self.btn_total.place( relx = 0.60,
                              rely = 0.23,
                              relheight = 0.5 ) 

        self.btn_generate_bill = tkinter.Button( 
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        background = 'AntiqueWhite4',
                        foreground = 'gold',
                        activeforeground = 'red',
                        activebackground = 'powder blue',
                        font = self.btn_font,
                        text = 'Generate Bill',
                        command = self.generate_reciept )
        self.btn_generate_bill.place( relx = 0.665,
                                      rely = 0.23,
                                      relheight = 0.5 )

        self.btn_clear = tkinter.Button( 
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        background = 'gray26',
                        foreground = 'gold',
                        activeforeground = 'red',
                        activebackground = 'powder blue',
                        font = self.btn_font,
                        text = 'Clear',
                        command = self.clear_values )
        self.btn_clear.place( relx = 0.784,
                              rely = 0.23,
                              relheight = 0.5 )

        self.btn_random = tkinter.Button( 
                self.lblfrm_billing_menu,
                borderwidth = 5,
                background = 'green',
                foreground = 'gold',
                activeforeground = 'red',
                activebackground = 'ghost white',
                font = self.btn_font,
                text = 'Random',
                command = self.create_random_billing_information )
        self.btn_random.place( relx = 0.849,
                               rely = 0.23,
                               relheight = 0.5 )

        self.btn_exit = tkinter.Button( 
                        self.lblfrm_billing_menu,
                        borderwidth = 5,
                        background = 'orchid1',
                        foreground = 'gold',
                        activeforeground = 'cyan',
                        activebackground = 'gray8',
                        font = self.btn_font,
                        text = 'Exit',
                        command = self.ask_quit )
        self.btn_exit.place( relx = 0.937,
                             rely = 0.23,
                             relheight = 0.5 )

#=======================Create Random Billing Information===============

    def generate_random_customer_name( self ):
        string_fullname = names.get_full_name( 
            gender = random.choice( ['male','female'] ))
        return( str( string_fullname ))

    def generate_random_mobile_number( self ):
        ''' Yes, well, cell phone number '''
        prefix = ['021', '022', '025', '027', '029']
        pre_cell = str( secrets.choice( prefix ))
        num_cell = str( secrets.randbits( 25 ))
        return( pre_cell + num_cell )

    def generate_random_bill_number( self ):
        return( str( secrets.token_hex( 6 )))

    def generate_random_integer( self ):
        # string_amount = str( random.randint( 0, 9 ))
        # return( string_amount )
        string_amount = random.randrange( 0, 11 )
        return( str( string_amount ))
 

    def create_random_billing_information( self ):
        self.customer_name.set( self.generate_random_customer_name())
        self.contact_number.set( self.generate_random_mobile_number())
        self.bill_number.set( self.generate_random_bill_number())
        #===============================================================
        self.bath_soap.set( self.generate_random_integer())
        self.face_cream.set( self.generate_random_integer())
        self.face_wash.set( self.generate_random_integer())
        self.hair_spray.set( self.generate_random_integer())
        self.hair_gel.set( self.generate_random_integer())
        self.body_lotion.set( self.generate_random_integer())
        #===============================================================
        self.rice.set( self.generate_random_integer())
        self.food_oil.set( self.generate_random_integer())
        self.red_lentil.set( self.generate_random_integer())
        self.wheat.set( self.generate_random_integer())
        self.sugar.set( self.generate_random_integer())
        self.tea.set( self.generate_random_integer())
        #===============================================================
        self.maaza.set( self.generate_random_integer())
        self.coke.set( self.generate_random_integer())
        self.frooti.set( self.generate_random_integer())
        self.thums_up.set( self.generate_random_integer())
        self.limca.set( self.generate_random_integer())
        self.sprite.set( self.generate_random_integer())

        


                               
        
if __name__ == '__main__':
    root = tkinter.Tk()
    application = Billing_Class( root )
    root.mainloop()