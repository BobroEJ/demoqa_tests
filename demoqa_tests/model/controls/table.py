from selene import have
from selene.support.shared import browser


class Table:

    def __init__(self, row_num):
        self.row_num = row_num

    def should_have(self, *results):
        if len(results) == 1:
            browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.exact_text(results[0]))
        else:
            for result in results:
                browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.text(result))

    '''
    OR W/O IF AND EXACT_TEXT:
    def should_have(self, *results):
        for result in results:
            browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.text(result))
    '''