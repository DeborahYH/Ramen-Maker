from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('800x600')
root.resizable(False,False)


# Creates tabs
custom_font = customtkinter.CTkFont("Helvetica", 15, "bold")

tabs = customtkinter.CTkTabview(root, width=400, height=300, fg_color="white", segmented_button_fg_color="#BEA69F", segmented_button_unselected_color="#BEA69F", segmented_button_selected_color="#9D796F", segmented_button_selected_hover_color="#D8CAC6", segmented_button_unselected_hover_color="#D8CAC6", text_color="#1F1817")
tabs._segmented_button.configure(font=custom_font)
tabs.pack(pady=50)

tab_1 = tabs.add("Base")
tab_2 = tabs.add("Toppings")
tab_3 = tabs.add("Appetizers")
tab_4 = tabs.add("Beverages")
tab_5 = tabs.add("Desserts")
tab_6 = tabs.add("Cart")

# Tab 1

frame_t = customtkinter.CTkFrame(tab_1, fg_color="#F2ECE6")
frame_t.pack(side="top", fill="both", expand=True)
frame_b = customtkinter.CTkFrame(tab_1, fg_color="#F2ECE6")
frame_b.pack(side="top", fill="both", expand=True)

frame_t1 = customtkinter.CTkFrame(frame_t, fg_color="#F2ECE6")
frame_t1.pack(side="left", fill="both", expand=True)
frame_t2 = customtkinter.CTkFrame(frame_t, fg_color="#F2ECE6")
frame_t2.pack(side="left", fill="both", expand=True)

lbl_size = customtkinter.CTkLabel(frame_t1, font=("Helvetica", 15, "bold", "underline"), text="Size")
lbl_size.pack(pady=5)

radio_s = customtkinter.CTkRadioButton(frame_t1, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3, font=("Helvetica", 15), text="Small")
radio_s.pack()
radio_m = customtkinter.CTkRadioButton(frame_t1, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Medium")
radio_m.pack()
radio_l = customtkinter.CTkRadioButton(frame_t1, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Large")
radio_l.pack()

lbl_broth = customtkinter.CTkLabel(frame_t2, font=("Helvetica", 15, "bold", "underline"), text="Soup Base")
lbl_broth.pack(pady=5)

radio_salt = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Salt")
radio_salt.pack()
radio_miso = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Miso")
radio_miso.pack()
radio_shoyu = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Shoyu")
radio_shoyu.pack()
radio_tonkotsu = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Tonkotsu")
radio_tonkotsu.pack()
radio_curry = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Curry")
radio_curry.pack()
radio_vegetarian = customtkinter.CTkRadioButton(frame_t2, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3,font=("Helvetica", 15), text="Vegetarian")
radio_vegetarian.pack()

slider_spice = customtkinter.CTkSlider(frame_b, from_ = 1, to = 5, number_of_steps = 5)
slider_spice.set(0)
slider_spice.pack(pady=(10,0))

lbl_spice = customtkinter.CTkLabel(frame_b, font=("Helvetica", 15), text="Spiciness Level")
lbl_spice.pack()


# Tab 2

frame_t = customtkinter.CTkFrame(tab_2, fg_color="#F2ECE6")
frame_t.pack(side="top", fill="both", expand=False)
frame_b = customtkinter.CTkFrame(tab_2, fg_color="#F2ECE6")
frame_b.pack(side="top", fill="both", expand=True)

frame_b1 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b1.pack(side="left", fill="both", expand=True)
frame_b2 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b2.pack(side="left", fill="both", expand=True)
frame_b3 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b3.pack(side="left", fill="both", expand=True)

lbl_toppings = customtkinter.CTkLabel(frame_t, font=("Helvetica", 15, "bold", "underline"), text="Toppings")
lbl_toppings.pack(pady=5)

top_1 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="beef")
top_1.pack()
top_2 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="pork")
top_2.pack()
top_3 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="chicken")
top_3.pack()
top_4 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="shrimp")
top_4.pack()
top_5 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="clams")
top_5.pack()
top_6 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="egg")
top_6.pack()
top_7 = customtkinter.CTkCheckBox(frame_b1, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="kamaboko")
top_7.pack()
top_8 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="shiitake")
top_8.pack()
top_9 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="shimeji")
top_9.pack()
top_10 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="kikurage")
top_10.pack()
top_11 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="negi")
top_11.pack()
top_12 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="bok choy")
top_12.pack()
top_13 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="moyashi")
top_13.pack()
top_14 = customtkinter.CTkCheckBox(frame_b2, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="peas")
top_14.pack()
top_15 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="corn")
top_15.pack()
top_16 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="carrots")
top_16.pack()
top_17 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="nori")
top_17.pack()
top_18 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="wakame")
top_18.pack()
top_19 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="kombu")
top_19.pack()
top_20 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="rayu")
top_20.pack()
top_21 = customtkinter.CTkCheckBox(frame_b3, checkbox_width=17, checkbox_height=17, border_width=2, hover_color="", font=("Helvetica", 15), text="mayu")
top_21.pack()


# Tab 3

frame_t = customtkinter.CTkFrame(tab_3, fg_color="#F2ECE6")
frame_t.pack(side="top", fill="both", expand=False)
frame_b = customtkinter.CTkFrame(tab_3, fg_color="#F2ECE6")
frame_b.pack(side="top", fill="both", expand=True)

frame_b1 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b1.pack(side="left", fill="both", expand=True)
frame_b2 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b2.pack(side="left", fill="both", expand=True)

line1 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line1.pack(side="top", fill="both", expand=False)
line2 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line2.pack(side="top", fill="both", expand=False)
line3 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line3.pack(side="top", fill="both", expand=False)
line4 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line4.pack(side="top", fill="both", expand=False)
line5 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line5.pack(side="top", fill="both", expand=False)
line6 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line6.pack(side="top", fill="both", expand=False)
line7 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line7.pack(side="top", fill="both", expand=False)
line8 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line8.pack(side="top", fill="both", expand=False)
line9 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line9.pack(side="top", fill="both", expand=False)
line10 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line10.pack(side="top", fill="both", expand=False)

lbl_appetizers = customtkinter.CTkLabel(frame_t, font=("Helvetica", 15, "bold", "underline"), text="Appetizers")
lbl_appetizers.pack(pady=5)

spinbox_1 = Spinbox(line1, width=3)
spinbox_1.pack(side="left", padx=(45,8), pady=7)
lbl_item_1 = customtkinter.CTkLabel(line1, font=("Helvetica", 15), text="Hiyayakko")
lbl_item_1.pack(side="left")

spinbox_2 = Spinbox(line2, width=3)
spinbox_2.pack(side="left", padx=(45,8), pady=7)
lbl_item_2 = customtkinter.CTkLabel(line2, font=("Helvetica", 15), text="Tsukemono")
lbl_item_2.pack(side="left")

spinbox_3 = Spinbox(line3, width=3)
spinbox_3.pack(side="left", padx=(45,8), pady=7)
lbl_item_3 = customtkinter.CTkLabel(line3, font=("Helvetica", 15), text="Wakame Salad")
lbl_item_3.pack(side="left")

spinbox_4 = Spinbox(line4, width=3)
spinbox_4.pack(side="left", padx=(45,8), pady=7)
lbl_item_4 = customtkinter.CTkLabel(line4, font=("Helvetica", 15), text="Edamame")
lbl_item_4.pack(side="left")

spinbox_5 = Spinbox(line5, width=3)
spinbox_5.pack(side="left", padx=(45,8), pady=7)
lbl_item_5 = customtkinter.CTkLabel(line5, font=("Helvetica", 15), text="Ceviche")
lbl_item_5.pack(side="left")

spinbox_6 = Spinbox(line6, width=3)
spinbox_6.pack(side="left", padx=(0,8), pady=7)
lbl_item_6 = customtkinter.CTkLabel(line6, font=("Helvetica", 15), text="Gyoza")
lbl_item_6.pack(side="left")

spinbox_7 = Spinbox(line7, width=3)
spinbox_7.pack(side="left", padx=(0,8), pady=7)
lbl_item_7 = customtkinter.CTkLabel(line7, font=("Helvetica", 15), text="Shumai")
lbl_item_7.pack(side="left")

spinbox_8 = Spinbox(line8, width=3)
spinbox_8.pack(side="left", padx=(0,8), pady=7)
lbl_item_8 = customtkinter.CTkLabel(line8, font=("Helvetica", 15), text="Takoyaki")
lbl_item_8.pack(side="left")

spinbox_9 = Spinbox(line9, width=3)
spinbox_9.pack(side="left", padx=(0,8), pady=7)
lbl_item_9 = customtkinter.CTkLabel(line9, font=("Helvetica", 15), text="Yakitori")
lbl_item_9.pack(side="left")

spinbox_10 = Spinbox(line10, width=3)
spinbox_10.pack(side="left", padx=(0,8), pady=7)
lbl_item_10 = customtkinter.CTkLabel(line10, font=("Helvetica", 15), text="Tempura")
lbl_item_10.pack(side="left")


# Tab 4

frame_t = customtkinter.CTkFrame(tab_4, fg_color="#F2ECE6")
frame_t.pack(side="top", fill="both", expand=False)
frame_b = customtkinter.CTkFrame(tab_4, fg_color="#F2ECE6")
frame_b.pack(side="top", fill="both", expand=True)

frame_b1 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b1.pack(side="left", fill="both", expand=True)
frame_b2 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b2.pack(side="left", fill="both", expand=True)

line1 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line1.pack(side="top", fill="both", expand=False)
line2 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line2.pack(side="top", fill="both", expand=False)
line3 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line3.pack(side="top", fill="both", expand=False)
line4 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line4.pack(side="top", fill="both", expand=False)
line5 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line5.pack(side="top", fill="both", expand=False)
line6 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line6.pack(side="top", fill="both", expand=False)

lbl_beverages = customtkinter.CTkLabel(frame_t, font=("Helvetica", 15, "bold", "underline"), text="Beverages")
lbl_beverages.pack(pady=5)

spin_bev1 = Spinbox(line1, width=3)
spin_bev1.pack(side="left", padx=(70,8), pady=7)
lbl_bev1 = customtkinter.CTkLabel(line1, font=("Helvetica", 15), text="Water")
lbl_bev1.pack(side="left")

spin_bev2 = Spinbox(line2, width=3)
spin_bev2.pack(side="left", padx=(70,8), pady=7)
lbl_bev2 = customtkinter.CTkLabel(line2, font=("Helvetica", 15), text="Coca-Cola")
lbl_bev2.pack(side="left")

spin_bev3 = Spinbox(line3, width=3)
spin_bev3.pack(side="left", padx=(70,8), pady=7)
lbl_bev3 = customtkinter.CTkLabel(line3, font=("Helvetica", 15), text="Ramune")
lbl_bev3.pack(side="left")

spin_bev4 = Spinbox(line4, width=3)
spin_bev4.pack(side="left", padx=(0,8), pady=7)
lbl_bev4 = customtkinter.CTkLabel(line4, font=("Helvetica", 15), text="Juice")
lbl_bev4.pack(side="left")

spin_bev5 = Spinbox(line5, width=3)
spin_bev5.pack(side="left", padx=(0,8), pady=7)
lbl_bev5 = customtkinter.CTkLabel(line5, font=("Helvetica", 15), text="Beer")
lbl_bev5.pack(side="left")

spin_bev6 = Spinbox(line6, width=3)
spin_bev6.pack(side="left", padx=(0,8), pady=7)
lbl_bev6 = customtkinter.CTkLabel(line6, font=("Helvetica", 15), text="Tea")
lbl_bev6.pack(side="left")


# Tab 5

frame_t = customtkinter.CTkFrame(tab_5, fg_color="#F2ECE6")
frame_t.pack(side="top", fill="both", expand=False)
frame_b = customtkinter.CTkFrame(tab_5, fg_color="#F2ECE6")
frame_b.pack(side="top", fill="both", expand=True)

frame_b1 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b1.pack(side="left", fill="both", expand=True)
frame_b2 = customtkinter.CTkFrame(frame_b, fg_color="#F2ECE6")
frame_b2.pack(side="left", fill="both", expand=True)

line1 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line1.pack(side="top", fill="both", expand=False)
line2 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line2.pack(side="top", fill="both", expand=False)
line3 = customtkinter.CTkFrame(frame_b1, fg_color="#F2ECE6")
line3.pack(side="top", fill="both", expand=False)
line4 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line4.pack(side="top", fill="both", expand=False)
line5 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line5.pack(side="top", fill="both", expand=False)
line6 = customtkinter.CTkFrame(frame_b2, fg_color="#F2ECE6")
line6.pack(side="top", fill="both", expand=False)

lbl_dessert = customtkinter.CTkLabel(frame_t, font=("Helvetica", 15, "bold", "underline"), text="Desserts")
lbl_dessert.pack(pady=5)

spin_des1 = Spinbox(line1, width=3)
spin_des1.pack(side="left", padx=(50,8), pady=7)
lbl_des1 = customtkinter.CTkLabel(line1, font=("Helvetica", 15), text="Coffee Jelly")
lbl_des1.pack(side="left")

spin_des2 = Spinbox(line2, width=3)
spin_des2.pack(side="left", padx=(50,8), pady=7)
lbl_des2 = customtkinter.CTkLabel(line2, font=("Helvetica", 15), text="Sakura Mochi")
lbl_des2.pack(side="left")

spin_des3 = Spinbox(line3, width=3)
spin_des3.pack(side="left", padx=(50,8), pady=7)
lbl_des3 = customtkinter.CTkLabel(line3, font=("Helvetica", 15), text="Ice Cream Mochi")
lbl_des3.pack(side="left")

spin_des4 = Spinbox(line4, width=3)
spin_des4.pack(side="left", padx=(0,8), pady=7)
lbl_des4 = customtkinter.CTkLabel(line4, font=("Helvetica", 15), text="Anmitsu")
lbl_des4.pack(side="left")

spin_des5 = Spinbox(line5, width=3)
spin_des5.pack(side="left", padx=(0,8), pady=7)
lbl_des5 = customtkinter.CTkLabel(line5, font=("Helvetica", 15), text="Matcha Cake")
lbl_des5.pack(side="left")

spin_des6 = Spinbox(line6, width=3)
spin_des6.pack(side="left", padx=(0,8), pady=7)
lbl_des6 = customtkinter.CTkLabel(line6, font=("Helvetica", 15), text="Matcha Tiramisu")
lbl_des6.pack(side="left")


# Tab 6

frame_left = customtkinter.CTkFrame(tab_6, fg_color="#B5F5FF")
frame_left.pack(side="left", fill="both", expand=True)
frame_right = customtkinter.CTkFrame(tab_6, fg_color="#FFCAEB")
frame_right.pack(side="left", fill="both", expand=True)

lbl_cart = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15, "bold", "underline"), text="Cart")
lbl_cart.pack()

item1 = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15), text="Item 1")
item1.pack()

item1_qtd = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15), text="Qtd")
item1_qtd.pack()

item1_price = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15), text="$0,00")
item1_price.pack()

lbl_delivery = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15, "bold", "underline"), text="Delivery")
lbl_delivery.pack()

delivery_price = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15), text="0")
delivery_price.pack()

lbl_coupon = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15, "bold", "underline"), text="Coupon")
lbl_coupon.pack()

lbl_total = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15, "bold", "underline"), text="Total")
lbl_total.pack()

total_price = customtkinter.CTkLabel(frame_left, font=("Helvetica", 15), text="0")
total_price.pack()

lbl_payment = customtkinter.CTkLabel(frame_right, font=("Helvetica", 15, "bold", "underline"), text="Payment Method")
lbl_payment.pack()

radio_pay_cash = customtkinter.CTkRadioButton(frame_right, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3, font=("Helvetica", 15), text="Cash")
radio_pay_cash.pack()

radio_pay_debit = customtkinter.CTkRadioButton(frame_right, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3, font=("Helvetica", 15), text="Debit")
radio_pay_debit.pack()

radio_pay_credit = customtkinter.CTkRadioButton(frame_right, radiobutton_width=15, radiobutton_height=15, border_width_unchecked=2, border_width_checked=3, font=("Helvetica", 15), text="Credit")
radio_pay_credit.pack()

btn_buy = customtkinter.CTkButton(frame_right, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Keep Buying", command = "back")
btn_buy.pack(pady=10)

btn_finish = customtkinter.CTkButton(frame_right, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Finish", command = "finish")
btn_finish.pack(pady=10)


root.mainloop()