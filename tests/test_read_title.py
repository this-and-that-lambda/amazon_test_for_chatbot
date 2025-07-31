def test_read_title(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    title = page.title()
    print(f" Page title is: {title}")
    assert title != ""
