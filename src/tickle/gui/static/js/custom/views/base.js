

export class BaseView
{

    constructor() {}

    _initProperties = (apiResponse) => {
        const thisObjectKeys = Object.keys(this);
            
        for (const key in apiResponse) {
            if (thisObjectKeys.includes(key)) {
                this[key] = apiResponse[key];
            }
        }
    }
}