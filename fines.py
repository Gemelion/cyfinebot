import requests
from bs4 import BeautifulSoup

def check_fines(id_number: str, car_number: str) -> list:
    url = "https://cycamerasystem.com.cy/Login"
    session = requests.Session()

    try:
        resp = session.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        token_input = soup.find("input", {"name": "__RequestVerificationToken"})
        token_value = token_input["value"] if token_input else ""
    except Exception:
        return []

    data = {
        "__RequestVerificationToken": token_value,
        "IDNumber": id_number,
        "CarRegistrationNumber": car_number
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        login_resp = session.post(url, data=data, headers=headers)
        login_soup = BeautifulSoup(login_resp.text, "html.parser")
    except Exception:
        return []

    fine_table = login_soup.find("table", class_="table")
    if not fine_table:
        return []

    fines = []
    for row in fine_table.find_all("tr")[1:]:
        cols = [td.text.strip() for td in row.find_all("td")]
        if cols:
            fines.append(cols)

    return fines
