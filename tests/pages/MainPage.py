from tests.pages.BasePage import BasePage


class MainPage(BasePage):
    new_advert_btn = '.new-advert-capture-container'
    open_modal_btn = '#auth'
    header_profile = '.mini-profile__capture'
    search_input = '.search__input'
    search_btn = '.search__button'
    lang_btn = '.lang-box'
    input_err = '.text-input_wrong'
    categories = '.root__category-container'
    category_href = '.root__category__content-categories-card-title'
    card = '.card__content'
    search_input = '.search__input'
    search_btn = '.search__button'
    empty = '#empty'
    lang_btn = '.lang-box'
    modal_window = '.modal-window'
    new_adv_btn = '.new-advert-capture-container'
    expand_menu = '.expand-menu__content'
    modal_backgroud = '.blackout'

    profile_link = '.expand-menu__sublabel:nth-of-type(1)'
    fav_link = '.expand-menu__sublabel:nth-of-type(2)'
    setting_link = '.expand-menu__sublabel:nth-of-type(3)'
    logout_btn = '#logout'

    login_email_div = '#logEmail'
    login_email_input = '#logEmail > .text-input__input'
    login_password_div = '#logPassword'
    login_password_input = '#logPassword > .text-input__input'
    login_btn = '#logButton'

    swith_to_reg_btn = '#overlay-sign-up'
    reg_email_div = '#regEmail'
    reg_email_input = '#regEmail > .text-input__input'
    reg_name_div = '#regName'
    reg_name_input = '#regName > .text-input__input'
    reg_surname_div = '#regSurname'
    reg_surname_input = '#regSurname > .text-input__input'
    reg_password_div = '#regPassword'
    reg_password_input = '#regPassword > .text-input__input'
    reg_reppassword_div = '#regRepPassword'
    reg_reppassword_input = '#regRepPassword > .text-input__input'
    reg_btn = '#regButton'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_login(self):
        elem = self.wait_render(self.open_modal_btn)
        elem.click()

    def click_new_adv(self):
        elem = self.wait_render(self.new_advert_btn)
        elem.click()

    def fill_login_email(self, value):
        self.fill_input(self.login_email_input, value)
    
    def fill_login_password(self, value):
        self.fill_input(self.login_password_input, value)

    def fill_reg_email(self, value):
        self.fill_input(self.reg_email_input, value)

    def fill_reg_name(self, value):
        self.fill_input(self.reg_name_input, value)

    def fill_reg_surname(self, value):
        self.fill_input(self.reg_surname_input, value)

    def fill_reg_password(self, value):
        self.fill_input(self.reg_password_input, value)

    def fill_reg_passwordRep(self, value):
        self.fill_input(self.reg_reppassword_input, value)

    def click_login_button(self):
        login_btn = self.wait_render(
            self.login_btn)
        login_btn.click()

    def click_reg_button(self):
        reg_btn = self.wait_render(self.reg_btn)
        reg_btn.click()

    def check_error(self):
        return self.is_exist(self.input_err)
    
    def check_reg_email_correct(self):
        email_div = self.wait_render(self.reg_email_div)
        return "text-input_correct" in email_div.get_attribute("class")
    
    def check_reg_name_correct(self):
        div = self.wait_render(self.reg_name_div)
        return "text-input_correct" in div.get_attribute("class")

    def check_reg_surname_correct(self):
        div = self.wait_render(self.reg_surname_div)
        return "text-input_correct" in div.get_attribute("class")
    
    def check_reg_password_correct(self):
        div = self.wait_render(self.reg_password_div)
        return "text-input_correct" in div.get_attribute("class")

    def is_logged(self):
        return self.is_exist(self.header_profile)

    def clear_log_inputs(self):
        self.wait_render(self.login_email_input).clear()
        self.wait_render(self.login_password_input).clear()

    def switch_to_reg(self):
        self.wait_render(self.swith_to_reg_btn).click()

    def clear_reg_email(self):
        self.wait_render(self.reg_email_input).clear()
    
    def clear_reg_name(self):
        self.wait_render(self.reg_name_input).clear()

    def clear_reg_surname(self):
        self.wait_render(self.reg_surname_input).clear()

    def clear_reg_password(self):
        self.wait_render(self.reg_password_input).clear()

    def clear_search_input(self):
        self.wait_render(self.search_input).clear()

    def is_categories_exist(self):
        return self.is_exist(self.categories)

    def is_card_grid_exist(self):
        return self.is_exist(self.card)

    def get_login_btn_text(self):
        return self.wait_render(self.open_modal_btn).get_attribute('innerHTML')

    def change_language(self):
        self.wait_click(self.lang_btn)

    def is_modal_active(self):
        return self.is_exist(self.modal_window)

    def close_modal(self):
        self.click_at_position(self.modal_backgroud, 1, 1)

    def open_profile_menu(self):
        self.wait_click(self.header_profile)

    def is_profile_menu_active(self):
        return self.is_exist(self.expand_menu)
    
    def click_logout_btn(self):
        self.wait_click(self.logout_btn)

    def is_login_btn_exist(self):
        return self.is_exist(self.open_modal_btn)

    def search_by_value_in_input(self, value):
        self.fill_input(self.search_input, value)
        self.wait_click(self.search_btn)
        self.wait_any_redirect('search')

    def is_search_empty(self):
        return self.is_exist(self.empty)