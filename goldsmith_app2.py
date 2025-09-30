import customtkinter
from tkinter import PhotoImage, StringVar
import os
import random
import time
from threading import Thread

# --- Define Custom Colors for Neon Reddish Theme ---
# These are hex codes for dark background with neon red accents
PRIMARY_DARK = "#0D0D0D" # Very dark background
NEON_RED_DARK = "#E74C3C" # Bright red for highlights (similar to #FF4040, #F00)
NEON_RED_LIGHT = "#FF6347" # Slightly lighter red for hover effects
ACCENT_GRAY = "#2C3E50" # Dark blue-gray for subtle elements
TEXT_COLOR = "#ECF0F1" # Light gray for general text
GOLD_COLOR = ("#B8860B", "#B8860B") # Keep gold for the login button

class LoginPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("GoldSmith App - Login")
        self.geometry("800x600")
        self.resizable(False, False)

        # Set appearance mode and custom theme
        customtkinter.set_appearance_mode("dark")
        # Configure window background (overrides default theme for root window)
        self.configure(fg_color=PRIMARY_DARK)

        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main frame for the glassmorphism effect
        self.glass_frame = customtkinter.CTkFrame(
            master=self,
            width=400,
            height=380,
            corner_radius=20,
            fg_color=("#1A1A1A", "#1A1A1A"), # Very dark gray, almost black to simulate transparency
            border_width=1,
            border_color=("#333333", "#333333") # A slightly lighter gray for the border
        )
        self.glass_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.glass_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.glass_frame.grid_columnconfigure(0, weight=1)

        # Title Label
        self.title_label = customtkinter.CTkLabel(
            master=self.glass_frame,
            text="GoldSmith App",
            font=customtkinter.CTkFont(family="Segoe UI", size=28, weight="bold"),
            text_color=NEON_RED_LIGHT # Neon red title
        )
        self.title_label.grid(row=0, column=0, pady=(40, 20), padx=30, sticky="n")

        # Username Input
        self.username_entry = customtkinter.CTkEntry(
            master=self.glass_frame,
            placeholder_text="Username",
            width=280,
            height=40,
            corner_radius=10,
            fg_color=ACCENT_GRAY, # Darker background for input fields
            text_color=TEXT_COLOR,
            font=customtkinter.CTkFont(family="Segoe UI", size=16),
            border_width=1,
            border_color=NEON_RED_DARK # Subtle thin neon red divider
        )
        self.username_entry.grid(row=1, column=0, pady=(20, 10))

        # Password Input
        self.password_entry = customtkinter.CTkEntry(
            master=self.glass_frame,
            placeholder_text="Password",
            width=280,
            height=40,
            corner_radius=10,
            show="*", # Hide password characters
            fg_color=ACCENT_GRAY,
            text_color=TEXT_COLOR,
            font=customtkinter.CTkFont(family="Segoe UI", size=16),
            border_width=1,
            border_color=NEON_RED_DARK # Subtle thin neon red divider
        )
        self.password_entry.grid(row=2, column=0, pady=(10, 30))

        # Login Button (Solid Gold)
        self.login_button = customtkinter.CTkButton(
            master=self.glass_frame,
            text="Login",
            width=280,
            height=50,
            corner_radius=10,
            fg_color=GOLD_COLOR, # DarkGoldenrod for both light/dark mode
            hover_color=("#D4AF37", "#D4AF37"), # Slightly lighter gold on hover
            text_color="#000000", # Black text for readability on gold
            font=customtkinter.CTkFont(family="Segoe UI", size=18, weight="bold"),
            command=self.login_event
        )
        self.login_button.grid(row=3, column=0, pady=(0, 40))

    def login_event(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "goldsmith" and password == "securepass":
            print("Login Successful!")
            self.destroy() # Close login window
            self.open_main_app() # Open the main application window
        else:
            print("Invalid Username or Password.")
            # Optionally show an error message in the UI
            if hasattr(self, 'error_label'):
                self.error_label.destroy()
            self.error_label = customtkinter.CTkLabel(self.glass_frame, text="Invalid credentials", text_color=NEON_RED_DARK)
            self.error_label.grid(row=4, column=0, pady=(0,10))
            self.after(3000, lambda: self.error_label.destroy() if hasattr(self, 'error_label') else None) # Remove error after 3 seconds

    def open_main_app(self):
        print("Opening main application...")
        main_app = MainApplication()
        main_app.mainloop()


class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GoldSmith App - Market Dashboard")
        self.geometry("1400x900") # Increased size for more content
        self.resizable(True, True)

        customtkinter.set_appearance_mode("dark")
        # No default color theme set here to allow direct fg_color on root window
        self.configure(fg_color=PRIMARY_DARK) # Set overall window background

        self.grid_rowconfigure(0, weight=0) # For title bar
        self.grid_rowconfigure(1, weight=1) # For main content
        self.grid_columnconfigure(0, weight=1)

        # Title Bar (Simulated with a label at the top)
        self.app_title_bar = customtkinter.CTkLabel(
            self,
            text="GoldSmith Market Tracker",
            font=customtkinter.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=NEON_RED_LIGHT,
            height=60,
            fg_color=ACCENT_GRAY, # Slightly lighter than background for depth
            corner_radius=10
        )
        self.app_title_bar.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,5))

        # Main content area below the title bar
        self.main_content_frame = customtkinter.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.main_content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.main_content_frame.grid_rowconfigure(0, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)

        # Tabbed Interface (CTkTabview)
        self.tab_view = customtkinter.CTkTabview(
            master=self.main_content_frame,
            segmented_button_fg_color=(ACCENT_GRAY, ACCENT_GRAY), # Background of tab buttons
            segmented_button_selected_color=(NEON_RED_DARK, NEON_RED_DARK), # Neon Red for selected tab
            segmented_button_selected_hover_color=(NEON_RED_LIGHT, NEON_RED_LIGHT), # Lighter Neon Red on hover
            segmented_button_unselected_color=(PRIMARY_DARK, PRIMARY_DARK), # Unselected tab button color (very dark)
            segmented_button_unselected_hover_color=(ACCENT_GRAY, ACCENT_GRAY), # Hover for unselected
            text_color=TEXT_COLOR, # Text color for tabs
            state="normal", # Ensure tabs are clickable
            # REMOVED: font=customtkinter.CTkFont(family="Segoe UI", size=16, weight="bold"), # This argument is not supported by CTkTabview itself
            height=700, # Adjust height as needed
            corner_radius=15, # Smooth edges for the tabview
            fg_color=(ACCENT_GRAY, ACCENT_GRAY), # Background of the tab content area
            border_width=1,
            border_color=NEON_RED_DARK, # Neon red border around the tab content
            command=self.on_tab_change # Command for tab change animation (if implemented)
        )
        self.tab_view.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add tabs
        self.tab_view.add("Live Rates")
        self.tab_view.add("Recent Orders") # Changed from Trades
        self.tab_view.add("Order Entry / Mgmt") # Changed from Orders
        self.tab_view.add("Gold Rates") # New Tab
        self.tab_view.add("Currency Diff.") # New Tab
        self.tab_view.add("Positions")
        self.tab_view.add("Trade History")
        self.tab_view.add("Order History")


        # --- Placeholder Content for each Tab ---
        self._setup_live_rates_tab()
        self._setup_recent_orders_tab()
        self._setup_order_entry_tab()
        self._setup_gold_rates_tab()
        self._setup_currency_diff_tab()
        self._setup_positions_tab()
        self._setup_trade_history_tab()
        self._setup_order_history_tab()


        # Initial data update (for placeholders)
        self.update_live_rates()
        self.update_gold_rates()
        self.update_currency_diff()
        self.update_recent_orders()


    def on_tab_change(self, selected_tab):
        """Placeholder for tab change animation or logic."""
        print(f"Tab changed to: {selected_tab}")
        # Here you could implement animations or specific data loading logic
        # For a simple fade effect (conceptual):
        # self.main_content_frame.fade_out() # (Requires custom implementation)
        # self.after(200, lambda: self.main_content_frame.fade_in()) # (Requires custom implementation)

    def _setup_live_rates_tab(self):
        live_rates_frame = self.tab_view.tab("Live Rates")
        live_rates_frame.grid_columnconfigure((0,1), weight=1)
        live_rates_frame.grid_rowconfigure((0,1,2,3), weight=1)

        # Section for specific metal rates (e.g., Gold, Silver)
        metal_rates_panel = customtkinter.CTkFrame(live_rates_frame, fg_color=PRIMARY_DARK, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        metal_rates_panel.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        metal_rates_panel.grid_columnconfigure((0,1,2,3), weight=1)
        metal_rates_panel.grid_rowconfigure((0,1), weight=1)

        customtkinter.CTkLabel(metal_rates_panel, text="Real-time Metal Rates", font=customtkinter.CTkFont(family="Segoe UI", size=18, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=0, column=0, columnspan=4, pady=5)

        # Gold Rate
        customtkinter.CTkLabel(metal_rates_panel, text="Gold (oz):", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.live_gold_rate_label = customtkinter.CTkLabel(metal_rates_panel, text="--.-- USD", font=customtkinter.CTkFont(size=16, weight="bold"), text_color=TEXT_COLOR)
        self.live_gold_rate_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        # Silver Rate
        customtkinter.CTkLabel(metal_rates_panel, text="Silver (oz):", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR).grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.live_silver_rate_label = customtkinter.CTkLabel(metal_rates_panel, text="--.-- USD", font=customtkinter.CTkFont(size=16, weight="bold"), text_color=TEXT_COLOR)
        self.live_silver_rate_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")


        # Placeholder for a live chart (e.g., Matplotlib embedding)
        chart_panel = customtkinter.CTkFrame(live_rates_frame, fg_color=ACCENT_GRAY, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        chart_panel.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        customtkinter.CTkLabel(chart_panel, text="[ Placeholder for Live Price Chart (e.g., Gold/Silver Spot) ]", font=customtkinter.CTkFont(size=18), text_color="gray70").pack(expand=True, fill="both", padx=20, pady=20)

        # Market News/Alerts
        news_panel = customtkinter.CTkFrame(live_rates_frame, fg_color=PRIMARY_DARK, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        news_panel.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        customtkinter.CTkLabel(news_panel, text="Market News / Alerts", font=customtkinter.CTkFont(family="Segoe UI", size=18, weight="bold"), text_color=NEON_RED_LIGHT).pack(pady=5)
        self.news_textbox = customtkinter.CTkTextbox(news_panel, wrap="word", height=100, fg_color=ACCENT_GRAY, text_color=TEXT_COLOR, border_color=NEON_RED_DARK, border_width=1)
        self.news_textbox.insert("end", "1. Gold prices stable ahead of Fed announcement.\n2. Silver demand rises in industrial sector.\n3. Breaking news goes here...")
        self.news_textbox.pack(fill="both", expand=True, padx=10, pady=10)

    def _setup_recent_orders_tab(self):
        recent_orders_frame = self.tab_view.tab("Recent Orders")
        recent_orders_frame.grid_columnconfigure(0, weight=1)
        recent_orders_frame.grid_rowconfigure(0, weight=1)

        # Example order data (for simulation)
        self.recent_orders_data = [
            {"ID": "001", "Type": "Buy", "Metal": "Gold", "Qty": "10g", "Price": "6500 INR/g", "Status": "Completed"},
            {"ID": "002", "Type": "Sell", "Metal": "Silver", "Qty": "100g", "Price": "80 INR/g", "Status": "Pending"},
            {"ID": "003", "Type": "Buy", "Metal": "Gold", "Qty": "50g", "Price": "6480 INR/g", "Status": "Completed"},
            {"ID": "004", "Type": "Sell", "Metal": "Gold", "Qty": "20g", "Price": "6550 INR/g", "Status": "Cancelled"},
            {"ID": "005", "Type": "Buy", "Metal": "Silver", "Qty": "200g", "Price": "79 INR/g", "Status": "Completed"},
        ]
        # Initial display will be handled by update_recent_orders() call in __init__

    def _setup_order_entry_tab(self):
        order_entry_frame = self.tab_view.tab("Order Entry / Mgmt")
        order_entry_frame.grid_columnconfigure((0,1), weight=1)
        order_entry_frame.grid_rowconfigure((0,1,2,3,4,5), weight=0) # Auto size for form

        customtkinter.CTkLabel(order_entry_frame, text="Place New Order", font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=0, column=0, columnspan=2, pady=10)

        # Input fields for order entry
        customtkinter.CTkLabel(order_entry_frame, text="Metal Type:", text_color=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=20, pady=5)
        self.metal_type_optionmenu = customtkinter.CTkOptionMenu(order_entry_frame, values=["Gold", "Silver", "Platinum"], fg_color=ACCENT_GRAY, text_color=TEXT_COLOR, button_color=NEON_RED_DARK, button_hover_color=NEON_RED_LIGHT)
        self.metal_type_optionmenu.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

        customtkinter.CTkLabel(order_entry_frame, text="Order Type:", text_color=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=20, pady=5)
        self.order_type_optionmenu = customtkinter.CTkOptionMenu(order_entry_frame, values=["Buy", "Sell"], fg_color=ACCENT_GRAY, text_color=TEXT_COLOR, button_color=NEON_RED_DARK, button_hover_color=NEON_RED_LIGHT)
        self.order_type_optionmenu.grid(row=2, column=1, sticky="ew", padx=20, pady=5)

        customtkinter.CTkLabel(order_entry_frame, text="Quantity (g/oz):", text_color=TEXT_COLOR).grid(row=3, column=0, sticky="w", padx=20, pady=5)
        self.quantity_entry = customtkinter.CTkEntry(order_entry_frame, placeholder_text="e.g., 10g or 1oz", fg_color=ACCENT_GRAY, text_color=TEXT_COLOR, border_color=NEON_RED_DARK)
        self.quantity_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=5)

        customtkinter.CTkLabel(order_entry_frame, text="Limit Price (optional):", text_color=TEXT_COLOR).grid(row=4, column=0, sticky="w", padx=20, pady=5)
        self.price_entry = customtkinter.CTkEntry(order_entry_frame, placeholder_text="e.g., 65000 (INR)", fg_color=ACCENT_GRAY, text_color=TEXT_COLOR, border_color=NEON_RED_DARK)
        self.price_entry.grid(row=4, column=1, sticky="ew", padx=20, pady=5)

        place_order_button = customtkinter.CTkButton(order_entry_frame, text="Place Order", command=self.place_order, fg_color=NEON_RED_DARK, hover_color=NEON_RED_LIGHT, text_color="#FFFFFF")
        place_order_button.grid(row=5, column=0, columnspan=2, pady=20)

    def _setup_gold_rates_tab(self):
        gold_rates_frame = self.tab_view.tab("Gold Rates")
        gold_rates_frame.grid_columnconfigure((0,1), weight=1)
        gold_rates_frame.grid_rowconfigure((0,1,2,3,4), weight=1)

        customtkinter.CTkLabel(gold_rates_frame, text="Gold Rates by Purity", font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=0, column=0, columnspan=2, pady=10)

        # Placeholder for 24K, 22K, 18K Gold Rates
        self.gold_24k_label = customtkinter.CTkLabel(gold_rates_frame, text="24 Carat Gold: Loading...", font=customtkinter.CTkFont(size=18), text_color=TEXT_COLOR)
        self.gold_24k_label.grid(row=1, column=0, columnspan=2, pady=5)
        self.gold_22k_label = customtkinter.CTkLabel(gold_rates_frame, text="22 Carat Gold: Loading...", font=customtkinter.CTkFont(size=18), text_color=TEXT_COLOR)
        self.gold_22k_label.grid(row=2, column=0, columnspan=2, pady=5)
        self.gold_18k_label = customtkinter.CTkLabel(gold_rates_frame, text="18 Carat Gold: Loading...", font=customtkinter.CTkFont(size=18), text_color=TEXT_COLOR)
        self.gold_18k_label.grid(row=3, column=0, columnspan=2, pady=5)

        # Last updated time
        self.gold_rates_update_time = customtkinter.CTkLabel(gold_rates_frame, text="Last Updated: --:--", font=customtkinter.CTkFont(size=14, slant="italic"), text_color="gray70")
        self.gold_rates_update_time.grid(row=4, column=0, columnspan=2, pady=(10,0), sticky="s")


    def _setup_currency_diff_tab(self):
        currency_diff_frame = self.tab_view.tab("Currency Diff.")
        currency_diff_frame.grid_columnconfigure((0,1,2), weight=1)
        currency_diff_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)

        customtkinter.CTkLabel(currency_diff_frame, text="Currency Exchange Rates", font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=0, column=0, columnspan=3, pady=10)

        # Header Row for currency table
        customtkinter.CTkLabel(currency_diff_frame, text="Pair", font=customtkinter.CTkFont(size=16, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=1, column=0, padx=5, pady=5)
        customtkinter.CTkLabel(currency_diff_frame, text="Rate", font=customtkinter.CTkFont(size=16, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=1, column=1, padx=5, pady=5)
        customtkinter.CTkLabel(currency_diff_frame, text="Change (24h)", font=customtkinter.CTkFont(size=16, weight="bold"), text_color=NEON_RED_LIGHT).grid(row=1, column=2, padx=5, pady=5)

        # Placeholder currency rates
        self.currency_usd_inr_label = customtkinter.CTkLabel(currency_diff_frame, text="USD/INR:", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_usd_inr_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.currency_usd_inr_rate = customtkinter.CTkLabel(currency_diff_frame, text="--.--", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_usd_inr_rate.grid(row=2, column=1, padx=5, pady=5)
        self.currency_usd_inr_change = customtkinter.CTkLabel(currency_diff_frame, text="--%", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_usd_inr_change.grid(row=2, column=2, padx=5, pady=5)

        self.currency_eur_inr_label = customtkinter.CTkLabel(currency_diff_frame, text="EUR/INR:", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_eur_inr_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.currency_eur_inr_rate = customtkinter.CTkLabel(currency_diff_frame, text="--.--", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_eur_inr_rate.grid(row=3, column=1, padx=5, pady=5)
        self.currency_eur_inr_change = customtkinter.CTkLabel(currency_diff_frame, text="--%", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_eur_inr_change.grid(row=3, column=2, padx=5, pady=5)

        self.currency_gbp_inr_label = customtkinter.CTkLabel(currency_diff_frame, text="GBP/INR:", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_gbp_inr_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.currency_gbp_inr_rate = customtkinter.CTkLabel(currency_diff_frame, text="--.--", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_gbp_inr_rate.grid(row=4, column=1, padx=5, pady=5)
        self.currency_gbp_inr_change = customtkinter.CTkLabel(currency_diff_frame, text="--%", font=customtkinter.CTkFont(size=16), text_color=TEXT_COLOR)
        self.currency_gbp_inr_change.grid(row=4, column=2, padx=5, pady=5)

        self.currency_diff_update_time = customtkinter.CTkLabel(currency_diff_frame, text="Last Updated: --:--", font=customtkinter.CTkFont(size=14, slant="italic"), text_color="gray70")
        self.currency_diff_update_time.grid(row=5, column=0, columnspan=3, pady=(10,0), sticky="s")


    def _setup_positions_tab(self):
        positions_frame = self.tab_view.tab("Positions")
        positions_frame.grid_columnconfigure(0, weight=1)
        positions_frame.grid_rowconfigure(0, weight=1)

        positions_table_frame = customtkinter.CTkFrame(positions_frame, fg_color=ACCENT_GRAY, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        positions_table_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        customtkinter.CTkLabel(positions_table_frame, text="[ Placeholder for Current Holdings / Open Positions Table ]", font=customtkinter.CTkFont(size=18), text_color="gray70").pack(expand=True, fill="both", padx=20, pady=20)

    def _setup_trade_history_tab(self):
        trade_history_frame = self.tab_view.tab("Trade History")
        trade_history_frame.grid_columnconfigure(0, weight=1)
        trade_history_frame.grid_rowconfigure(0, weight=1)

        history_table_frame = customtkinter.CTkFrame(trade_history_frame, fg_color=ACCENT_GRAY, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        history_table_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        customtkinter.CTkLabel(history_table_frame, text="[ Placeholder for Historical Trade Records Table ]", font=customtkinter.CTkFont(size=18), text_color="gray70").pack(expand=True, fill="both", padx=20, pady=20)

    def _setup_order_history_tab(self):
        order_history_frame = self.tab_view.tab("Order History")
        order_history_frame.grid_columnconfigure(0, weight=1)
        order_history_frame.grid_rowconfigure(0, weight=1)

        order_history_table_frame = customtkinter.CTkFrame(order_history_frame, fg_color=ACCENT_GRAY, corner_radius=10, border_width=1, border_color=NEON_RED_DARK)
        order_history_table_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        customtkinter.CTkLabel(order_history_table_frame, text="[ Placeholder for Historical Order Records Table ]", font=customtkinter.CTkFont(size=18), text_color="gray70").pack(expand=True, fill="both", padx=20, pady=20)


    # --- Dummy Data Update Functions (for demonstration) ---
    def update_live_rates(self):
        # Simulate fetching live rates
        gold_rate = round(random.uniform(2300.00, 2400.00), 2)
        silver_rate = round(random.uniform(28.00, 32.00), 2)
        self.live_gold_rate_label.configure(text=f"{gold_rate:.2f} USD")
        self.live_silver_rate_label.configure(text=f"{silver_rate:.2f} USD")
        self.after(5000, self.update_live_rates) # Update every 5 seconds

    def update_gold_rates(self):
        # Simulate different purity rates in INR (per 10g or per 1g, adjust as needed)
        base_rate = round(random.uniform(6500.00, 6800.00), 2) # per gram for 24K
        self.gold_24k_label.configure(text=f"24 Carat Gold: {base_rate:.2f} INR/g")
        self.gold_22k_label.configure(text=f"22 Carat Gold: {base_rate * 0.916:.2f} INR/g") # 91.6% purity
        self.gold_18k_label.configure(text=f"18 Carat Gold: {base_rate * 0.75:.2f} INR/g") # 75% purity
        self.gold_rates_update_time.configure(text=f"Last Updated: {time.strftime('%H:%M:%S')}")
        self.after(10000, self.update_gold_rates) # Update every 10 seconds

    def update_currency_diff(self):
        # Simulate currency rates against INR
        usd_inr = round(random.uniform(82.00, 83.50), 2)
        eur_inr = round(random.uniform(89.00, 91.00), 2)
        gbp_inr = round(random.uniform(105.00, 107.00), 2)

        # Simulate small random change (e.g., +/- 0.5%)
        usd_change = round(random.uniform(-0.5, 0.5), 2)
        eur_change = round(random.uniform(-0.5, 0.5), 2)
        gbp_change = round(random.uniform(-0.5, 0.5), 2)

        self.currency_usd_inr_rate.configure(text=f"{usd_inr:.2f}")
        self.currency_usd_inr_change.configure(text=f"{usd_change:+.2f}%", text_color=NEON_RED_DARK if usd_change > 0 else "#2ECC71") # Green for positive
        self.currency_eur_inr_rate.configure(text=f"{eur_inr:.2f}")
        self.currency_eur_inr_change.configure(text=f"{eur_change:+.2f}%", text_color=NEON_RED_DARK if eur_change > 0 else "#2ECC71")
        self.currency_gbp_inr_rate.configure(text=f"{gbp_inr:.2f}")
        self.currency_gbp_inr_change.configure(text=f"{gbp_change:+.2f}%", text_color=NEON_RED_DARK if gbp_change > 0 else "#2ECC71")

        self.currency_diff_update_time.configure(text=f"Last Updated: {time.strftime('%H:%M:%S')}")
        self.after(7000, self.update_currency_diff) # Update every 7 seconds

    def update_recent_orders(self):
        recent_orders_frame = self.tab_view.tab("Recent Orders")
        # Clear previous content to avoid duplicates on update
        for widget in recent_orders_frame.winfo_children():
            widget.destroy()

        customtkinter.CTkLabel(recent_orders_frame, text="Recent Orders (Last 24h)", font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="bold"), text_color=NEON_RED_LIGHT).pack(pady=10)

        # Create headers
        header_frame = customtkinter.CTkFrame(recent_orders_frame, fg_color=PRIMARY_DARK)
        header_frame.pack(fill="x", padx=10, pady=(0,5))
        header_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        headers = ["ID", "Type", "Metal", "Qty", "Price", "Status"]
        for i, header in enumerate(headers):
            customtkinter.CTkLabel(header_frame, text=header, font=customtkinter.CTkFont(size=14, weight="bold"), text_color=NEON_RED_DARK).grid(row=0, column=i, padx=5, sticky="ew")

        # Create a scrollable frame for orders
        scrollable_orders_frame = customtkinter.CTkScrollableFrame(recent_orders_frame, fg_color=ACCENT_GRAY, corner_radius=10, height=200)
        scrollable_orders_frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollable_orders_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)

        # Populate orders
        for r, order in enumerate(self.recent_orders_data):
            row = r + 1 # Start from row 1 after header
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["ID"], font=customtkinter.CTkFont(size=14), text_color=TEXT_COLOR).grid(row=row, column=0, padx=5, pady=2, sticky="ew")
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["Type"], font=customtkinter.CTkFont(size=14), text_color="#2ECC71" if order["Type"] == "Buy" else NEON_RED_DARK).grid(row=row, column=1, padx=5, pady=2, sticky="ew")
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["Metal"], font=customtkinter.CTkFont(size=14), text_color=TEXT_COLOR).grid(row=row, column=2, padx=5, pady=2, sticky="ew")
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["Qty"], font=customtkinter.CTkFont(size=14), text_color=TEXT_COLOR).grid(row=row, column=3, padx=5, pady=2, sticky="ew")
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["Price"], font=customtkinter.CTkFont(size=14), text_color=TEXT_COLOR).grid(row=row, column=4, padx=5, pady=2, sticky="ew")
            customtkinter.CTkLabel(scrollable_orders_frame, text=order["Status"], font=customtkinter.CTkFont(size=14), text_color=TEXT_COLOR).grid(row=row, column=5, padx=5, pady=2, sticky="ew")

        # Add a refresh button
        refresh_button = customtkinter.CTkButton(recent_orders_frame, text="Refresh Orders", command=self.simulate_new_order_data, fg_color=NEON_RED_DARK, hover_color=NEON_RED_LIGHT, text_color="#FFFFFF")
        refresh_button.pack(pady=10)


    def place_order(self):
        metal_type = self.metal_type_optionmenu.get()
        order_type = self.order_type_optionmenu.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if not quantity:
            print("Please enter a quantity.")
            # Show error in UI
            return

        print(f"Placing {order_type} order for {quantity} of {metal_type} at {price if price else 'Market Price'}")
        # In a real app, this would send data to a backend.
        # For now, simulate adding a new order to the recent orders list
        new_order_id = f"00{len(self.recent_orders_data) + 1}"
        new_order_status = "Pending" if price else "Completed"
        self.recent_orders_data.insert(0, { # Insert at the beginning to show as "most recent"
            "ID": new_order_id,
            "Type": order_type,
            "Metal": metal_type,
            "Qty": quantity,
            "Price": price if price else "Market",
            "Status": new_order_status
        })
        self.quantity_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.tab_view.set("Recent Orders") # Switch to recent orders tab
        self.update_recent_orders() # Update the list

    def simulate_new_order_data(self):
        # Simulate receiving new order data
        new_order_id = f"00{len(self.recent_orders_data) + 1}"
        metals = ["Gold", "Silver"]
        types = ["Buy", "Sell"]
        quantities = ["5g", "10g", "1oz", "20g", "50oz", "100g"]
        prices = ["6600 INR/g", "82 INR/g", "Market", "6550 INR/g", "79 INR/g"]
        statuses = ["Completed", "Pending", "Cancelled"]

        simulated_order = {
            "ID": new_order_id,
            "Type": random.choice(types),
            "Metal": random.choice(metals),
            "Qty": random.choice(quantities),
            "Price": random.choice(prices),
            "Status": random.choice(statuses)
        }
        self.recent_orders_data.insert(0, simulated_order) # Add to the top
        self.update_recent_orders() # Refresh the display


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()