import customtkinter
from tkinter import PhotoImage
import os

class LoginPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("GoldSmith App - Login")
        self.geometry("800x600")
        self.resizable(False, False)

        # Set appearance mode and color theme
        customtkinter.set_appearance_mode("dark") # Deep black/dark background
        customtkinter.set_default_color_theme("blue") # You can experiment with "dark-blue" or "green"

        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Background image (optional, but can enhance the deep black/dark feel)
        # For a true deep black, a simple background color might be enough.
        # If you want to use an image, uncomment and provide a path:
        # try:
        #     self.bg_image = PhotoImage(file="path/to/your/dark_background_image.png")
        #     self.bg_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        #     self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # except Exception as e:
        #     print(f"Could not load background image: {e}. Using solid color background.")
        #     self.configure(fg_color="gray10") # Fallback to a very dark gray/black

        # Main frame for the glassmorphism effect
        # We simulate glassmorphism by using a semi-transparent background color
        # and a border. True blurring of elements *behind* the frame is
        # not directly supported in CustomTkinter (it's a CSS `backdrop-filter` property).
        # We can achieve a similar visual feel with transparency and colors.
        self.glass_frame = customtkinter.CTkFrame(
            master=self,
            width=400,
            height=380,
            corner_radius=20,  # Softly blurred edges
            # ************ THIS IS THE CORRECTED LINE ************
            fg_color=("#1A1A1A", "#1A1A1A"), # Very dark gray, almost black to simulate transparency
            border_width=1,
            # ************ THIS IS THE CORRECTED LINE ************
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
            text_color="#FFFFFF" # White text for contrast
        )
        self.title_label.grid(row=0, column=0, pady=(40, 20), padx=30, sticky="n")

        # Username Input
        self.username_entry = customtkinter.CTkEntry(
            master=self.glass_frame,
            placeholder_text="Username",
            width=280,
            height=40,
            corner_radius=10,
            fg_color=("gray20", "gray20"), # Darker background for input fields
            text_color="#FFFFFF",
            font=customtkinter.CTkFont(family="Segoe UI", size=16),
            border_width=1,
            border_color="gray30" # Subtle thin divider
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
            fg_color=("gray20", "gray20"),
            text_color="#FFFFFF",
            font=customtkinter.CTkFont(family="Segoe UI", size=16),
            border_width=1,
            border_color="gray30" # Subtle thin divider
        )
        self.password_entry.grid(row=2, column=0, pady=(10, 30))

        # Login Button (Solid Gold)
        self.login_button = customtkinter.CTkButton(
            master=self.glass_frame,
            text="Login",
            width=280,
            height=50,
            corner_radius=10,
            # Solid gold color (hex codes)
            fg_color=("#B8860B", "#B8860B"), # DarkGoldenrod for both light/dark mode
            hover_color=("#D4AF37", "#D4AF37"), # Slightly lighter gold on hover
            text_color="#000000", # Black text for readability on gold
            font=customtkinter.CTkFont(family="Segoe UI", size=18, weight="bold"),
            command=self.login_event
        )
        self.login_button.grid(row=3, column=0, pady=(0, 40))

    def login_event(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple placeholder for authentication
        # In a real application, you would check against a database or secure system
        if username == "goldsmith" and password == "securepass":
            print("Login Successful!")
            self.destroy() # Close login window
            self.open_main_app() # Open the main application window
        else:
            print("Invalid Username or Password.")
            # Optionally show an error message in the UI
            # self.error_label = customtkinter.CTkLabel(self.glass_frame, text="Invalid credentials", text_color="red")
            # self.error_label.grid(row=4, column=0)

    def open_main_app(self):
        # This function will be called upon successful login
        # We will define the main application window in the next step
        print("Opening main application...")
        # For now, let's just create a placeholder main window
        main_app = MainApplication()
        main_app.mainloop()


class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GoldSmith App - Market Dashboard")
        self.geometry("1200x800")
        self.resizable(True, True)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title Bar (Simulated with a label at the top)
        self.app_title_bar = customtkinter.CTkLabel(
            self,
            text="GoldSmith Market Tracker",
            font=customtkinter.CTkFont(family="Segoe UI", size=24, weight="bold"),
            text_color="#FFFFFF",
            height=50,
            fg_color="gray15" # Slightly lighter than background for depth
        )
        self.app_title_bar.grid(row=0, column=0, columnspan=1, sticky="ew", pady=(0,5))

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
            segmented_button_fg_color=("gray10", "gray10"), # Background of tab buttons
            segmented_button_selected_color=("#B8860B", "#B8860B"), # Gold for selected tab
            segmented_button_selected_hover_color=("#D4AF37", "#D4AF37"), # Lighter gold on hover
            segmented_button_unselected_color=("gray20", "gray20"), # Unselected tab button color
            segmented_button_unselected_hover_color=("gray30", "gray30"), # Hover for unselected
            text_color="#FFFFFF", # Text color for tabs
            state="normal", # Ensure tabs are clickable
            font=customtkinter.CTkFont(family="Segoe UI", size=16, weight="bold"),
            height=700, # Adjust height as needed
            corner_radius=15, # Smooth edges for the tabview
            fg_color=("gray15", "gray15"), # Background of the tab content area
            border_width=1,
            border_color="gray30"
        )
        self.tab_view.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add tabs
        self.tab_view.add("Live Rates")
        self.tab_view.add("Trades")
        self.tab_view.add("Orders")
        self.tab_view.add("Positions")
        self.tab_view.add("Trade History")
        self.tab_view.add("Order History")

        # --- Placeholder Content for each Tab ---

        # Live Rates Tab
        live_rates_frame = self.tab_view.tab("Live Rates")
        live_rates_frame.grid_columnconfigure(0, weight=1)
        live_rates_frame.grid_rowconfigure(0, weight=1)
        # Example: A placeholder for a chart or data table
        live_rates_label = customtkinter.CTkLabel(
            live_rates_frame,
            text="Live Rates Chart/Table Goes Here",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        live_rates_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Trades Tab
        trades_frame = self.tab_view.tab("Trades")
        trades_label = customtkinter.CTkLabel(
            trades_frame,
            text="Recent Trades List",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        trades_label.pack(padx=20, pady=20)

        # Orders Tab
        orders_frame = self.tab_view.tab("Orders")
        orders_label = customtkinter.CTkLabel(
            orders_frame,
            text="Pending Orders / Order Entry",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        orders_label.pack(padx=20, pady=20)

        # Positions Tab
        positions_frame = self.tab_view.tab("Positions")
        positions_label = customtkinter.CTkLabel(
            positions_frame,
            text="Current Holdings / Open Positions",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        positions_label.pack(padx=20, pady=20)

        # Trade History Tab
        trade_history_frame = self.tab_view.tab("Trade History")
        trade_history_label = customtkinter.CTkLabel(
            trade_history_frame,
            text="Historical Trade Records",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        trade_history_label.pack(padx=20, pady=20)

        # Order History Tab
        order_history_frame = self.tab_view.tab("Order History")
        order_history_label = customtkinter.CTkLabel(
            order_history_frame,
            text="Historical Order Records",
            font=customtkinter.CTkFont(family="Segoe UI", size=20),
            text_color="gray70"
        )
        order_history_label.pack(padx=20, pady=20)


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()