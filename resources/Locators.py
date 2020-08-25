from selenium.webdriver.common.by import By

class Locators():
    """Store how web elements are being located"""

    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON=(By.XPATH,"//div[@class='nav-right']//input[@class='nav-input']") 

    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK=(By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[1]")

    # --- Product Details Page Locators ---
    ADD_TO_CART_BUTTON=(By.ID, "add-to-cart-button")

    # --- Sub Cart Page Locators ---
    SUB_CART_DIV=(By.ID,"hlb-subcart")
    CART_BUTTON=(By.ID,"hlb-view-cart-announce")
    PROCEED_TO_BUY_BUTTON=(By.ID,"hlb-ptc-btn-native")
    CART_COUNT=(By.ID,"nav-cart-count")
    
    # --- Cart Page Locators ---
    DELETE_ITEM_LINK=(By.XPATH,"//div[contains(@class,'a-row sc-action-links')]//input[contains(@data-action,'delete')]")
    CART_COUNT=(By.ID,'nav-cart-count')
    PROCEED_TO_CHECKOUT_BUTTON=(By.NAME,"proceedToRetailCheckout")
    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX=(By.ID,"ap_email")
