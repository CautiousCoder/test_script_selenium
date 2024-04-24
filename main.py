from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()


# Login Wordpress site
def login(base_url, uname, password):
    driver.get(f"{base_url}/wp-login.php")

    # access the field
    uname_field = driver.find_element(By.ID, "user_login")
    password_field = driver.find_element(By.ID, "user_pass")
    login_btn = driver.find_element(By.ID, "wp-submit")

    # fill the field and login
    uname_field.send_keys(uname)
    password_field.send_keys(password)
    login_btn.click()
    driver.implicitly_wait(2)

    try:
        # check wp-dark-mode plugin install or not
        check_plugin_installed(base_url)
    except Exception as e:
        print("Some error occur -", e)
    
    time.sleep(10)
    driver.close()
    driver.quit()


# check plugin install or not
def check_plugin_installed(base_url):
    driver.get(f"{base_url}/wp-admin/plugins.php")

    # wating for page load
    WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.ID, "the-list"))
    )
    plugin_name = "WP Dark Mode"
    try:
        driver.find_element(By.XPATH, f"//tr[contains(@class, 'active')]//strong[text()='{plugin_name}']")
        try:
            driver.find_element(By.CLASS_NAME, "inactive")
            driver.find_element(By.LINK_TEXT, "Activate").click()
            enable_backend_dark_mode(base_url)
        except Exception as e:
            print("Plugin already activate")
            enable_backend_dark_mode(base_url)
    except Exception as e:
        print("Plugin not found. Now install...")
        driver.get(f"{base_url}/wp-admin/plugin-install.php")

        # wating for page load
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "upload-view-toggle"))
        )

        # Plugin file path
        file = 'C:/xampp/htdocs/test/wp-dark-mode.5.0.4.zip'
        #upload the plugin
        driver.find_element(By.CLASS_NAME, "upload-view-toggle").click()
        try:
            # Wait for the file input element to be clickable
            file_input = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@type="file"]'))
            )
            
            # Send the path of the zip file to the file input element
            file_input.send_keys(file)
            
            print("File uploaded successfully!")
        except Exception as e:
            print("Error uploading file:", e)
        driver.find_element(By.ID, "install-plugin-submit").click()
        driver.implicitly_wait(1)
        try:
            driver.find_element(By.LINK_TEXT, "Activate Plugin").click()
            enable_backend_dark_mode(base_url)
        except Exception as e:
            print("Could nod active plugin", e)
        driver.implicitly_wait(1)


# enable dark mode for backend
def enable_backend_dark_mode(base_url):
    # click Wp dark mode plugin option
    driver.find_element(By.CLASS_NAME, "toplevel_page_wp-dark-mode").click()
    # click Admin Panel Dark Mode
    driver.find_element(By.LINK_TEXT, "Admin Panel Dark Mode")
    dark_btn = 'Enable Admin Dashboard Dark Mode'
    try:
        driver.find_element(By.CLASS_NAME, "bg-slate-200")
        try:
            driver.find_element(By.XPATH, f"//label[contains(@class, 'w-fit')]//div[text()='{dark_btn}']").click()
            save_change_text = 'Save Changes'
            driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']").click()
            driver.implicitly_wait(2)
            check_backend_darkmode(base_url)
        except Exception as e:
            print("Some Error Occur - ", e)
    except Exception as e:
        print("Already Enable Admin Dashboard Dark Mode")
        check_backend_darkmode(base_url)


# check dark mode work or not
def check_backend_darkmode(base_url):
    try:
        backend_dark_btn = driver.find_element(By.XPATH, f"//li[contains(@class, 'wp-dark-mode-admin-bar-switch')]")
        check_mode = backend_dark_btn.is_displayed()
        assert check_mode == True
        backend_dark_btn.click()
        dark_mode_active = driver.find_element(By.CLASS_NAME, "wp-dark-mode-active")
        if dark_mode_active:
            print("Back-end Dark Mode work successfully.")
        else:
            print("Back-end Dark Mode not work Properly.")
        switch_setting(base_url)
    except Exception as e:
        print("Error present in backend dark mode option",e)


# switch setting option
def switch_setting(base_url):
    driver.get(f"{base_url}/wp-admin/admin.php?page=wp-dark-mode#/frontend")
    setting_text = 'Customization'
    try:
        driver.find_element(By.XPATH, f"//div[contains(@class, 'wp-dark-mode-admin-sidebar-nav-container')]//h4[text()='{setting_text}']").click()
        driver.find_element(By.LINK_TEXT, "Switch Settings").click()
        
    except Exception as e:
        print("Could not find Switch Setting - ",e)

    driver.implicitly_wait(3)
    # change floting switch style
    floting_switch_style()

    driver.implicitly_wait(3)
    # change floting switch size
    floting_switch_size()

    driver.implicitly_wait(3)
    # change floting switch position
    floting_switch_position()

    driver.implicitly_wait(3)
    # Disable shortcut option
    shortcut_setting_off()

    driver.implicitly_wait(3)
    # change animation option
    switch_animation_setting(base_url)

    driver.implicitly_wait(3)
    # check frontend dark mode work or not
    check_frontend_dark_mode(base_url)
    

# Floating Switch Styles
def floting_switch_style():
    light_text = 'Light'
    try:
        driver.find_element(By.XPATH, f"//div[contains(@class, 'wp-dark-mode-switch')]//span[text()='{light_text}']")
        driver.implicitly_wait(1)
        save_change_text = 'Save Changes'
        save_changes_btn = driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']")
        save_changes_btn.click()
        save_changes_btn.clear()
    except Exception as e:
        print("Already Change default option - ",e)


# Floating Switch Sizes
def floting_switch_size():
    custom_text = 'Custom'
    save_change_text = 'Save Changes'
    try:
        driver.find_element(By.XPATH, f"//div[contains(@class, 'text-base')]//span[text()='{custom_text}']").click()
        driver.implicitly_wait(1)
        size_input = driver.find_element(By.XPATH, f"//input[contains(@class, 'appearance-none')]")
        size_input.clear()
        size_input.send_keys(220)
        save_changes_btn = driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']")
        save_changes_btn.click()
        save_changes_btn.clear()
    except Exception as e:
        print("Already change to custom option - ",e)
    
    
# Floating Switch Sizes
def floting_switch_position():
    position_text = 'Left'
    save_change_text = 'Save Changes'
    try:
        driver.find_element(By.XPATH, f"//div[contains(@class, 'text-base')]//span[text()='{position_text}']").click()
        driver.implicitly_wait(1)
        save_changes_btn = driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']")
        save_changes_btn.click()
        save_changes_btn.clear()
    except Exception as e:
        print("Already change to custom position - ",e)
    

#Accessibility shortcut setting off
def shortcut_setting_off():
    driver.find_element(By.LINK_TEXT, "Accessibility").click()
    shortcut_text = 'Keyboard Shortcut'
    try:
        driver.find_element(By.XPATH, f"//label[contains(@class, 'w-fit')]//div[text()='{shortcut_text}']").click()
        save_change_text = 'Save Changes'
        driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']").click()
    except Exception as e:
        print("Already disable shortcut key option - ",e)


# Animation effect
def switch_animation_setting(base_url):
    driver.get(f"{base_url}/wp-admin/admin.php?page=wp-dark-mode#/switch")
    animation_text = 'Switch Attention Effect '
    list_text = 'Vibrate'
    try:
        driver.find_element(By.XPATH, f"//label[contains(@class, 'w-fit')]//div[text()='{animation_text}']").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, f"//div[contains(@class, 'text-base')]//span[text()='{list_text}']").click()
        driver.implicitly_wait(2)
        save_change_text = 'Save Changes'
        driver.find_element(By.XPATH, f"//button[text()='{save_change_text}']").click()
    except Exception as e:
        print("Some error occur to enable Switch Attention Effect -",e)


# check frontend dark mode work or not
def check_frontend_dark_mode(base_url):
    driver.get(f"{base_url}")
    try:
        frontend_darkmode_btn = driver.find_element(By.CLASS_NAME, "wp-dark-mode-switch")
        check_btn = frontend_darkmode_btn.is_displayed()
        assert check_btn == True
        frontend_darkmode_btn.click()
        dark_mode_active = driver.find_element(By.CLASS_NAME, "wp-dark-mode-active")
        if dark_mode_active:
            print("Front-end Dark Mode work successfully.")
        else:
            print("Front-end Dark Mode not work Properly.")

    except Exception as e:
        print("Error occur frontend dark mode option",e)  


def main():
    base_url = "http://localhost/test"
    user_name = "test"
    user_password = "123456"
    login(base_url, user_name, user_password)


if __name__ == "__main__":
    main()