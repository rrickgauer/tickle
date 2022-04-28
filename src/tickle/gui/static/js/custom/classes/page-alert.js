

export class PageAlert
{

    static init() {
        $(PageAlert.Elements.CONTAINER).on('close.bs.alert', function(e) {
            console.log('close');
            e.preventDefault();
            PageAlert.hide();
        });
    }

    static show() {
        $(PageAlert.Elements.CONTAINER).removeClass('d-none');
    }

    static hide() {
        $(PageAlert.Elements.CONTAINER).addClass('d-none');
    }

    static resetTexts() {
        PageAlert.setBoldText('');
        PageAlert.setNormalText('');
    }

    static setBoldText(text) {
        $(PageAlert.Elements.TEXT_BOLD).text(text);
    }

    static setNormalText(text) {
        $(PageAlert.Elements.TEXT_NORMAL).text(text);
    }
}

PageAlert.Elements = {
    CONTAINER: '#page-alert',
    TEXT_BOLD: '#page-alert-text-bold',
    TEXT_NORMAL: '#page-alert-text-normal',
}