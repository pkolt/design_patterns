/*
* Модуль (Module) - паттерн, структурирующий объекты.
*
* Задачи:
*
*   1. Инкапсуляция
*   2. Создание четкой структуры из подключаемых модулей
*   3. Не засорять глобальный контекст
*
* */


(function(global, window, document, undefined){

    function Module(){
        var privateVar = 0;
        return {
            getPrivateVar: function(){
                return privateVar;
            }
        }
    }

    global.myModule = new Module;

})(this, window, window.document, undefined);


console.log(myModule.privateVar);  // undefined
console.log(myModule.getPrivateVar());  // 0
