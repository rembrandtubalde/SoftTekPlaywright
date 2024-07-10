import pytest
from playwright.sync_api import Page
from Login.Create_User import User_Functions  # Asegúrate de que la ruta sea correcta

@pytest.fixture(scope="function")
def page_context(playwright):
    """Inicializa el navegador y el contexto de la página para cada prueba."""
    browser = playwright.chromium.launch(headless=False)  # Cambiar a headless=True para ejecuciones en background
    page = browser.new_page()
    yield page
    browser.close()

def test_login(page_context: Page):
    cu = User_Functions(page_context)
    cu.login('Admin', 'admin123')
    random_letter = cu.generate_random_letter()
    id_user = cu.fill_user_details('Jhon', 'Peter', 'Pérez', f"JhonPePe{random_letter}", 'JhoPePe123.', 'JhoPePe123.')
    cu.verify_user_creation("//h6[contains(.,'Personal Details')]")
    cu.verify_employee_information(id_user)
