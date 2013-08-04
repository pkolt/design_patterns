/*
* Одиночка (Singleton) - паттерн, порождающий объекты.
*
* Гарантирует, что у класса есть только один экземпляр,
* и предоставляет к нему глобальную точку доступа.
*
 */


function Singleton(){
    var instance;

    // переопределяем конструктор
    Singleton = function(){
        return instance;
    };

    // переносим свойства прототипа
    Singleton.prototype = this;

    // создаем экземпляр
    instance = new Singleton();

    // переустанавливаем указатель на конструктор
    instance.constructor = Singleton;

    return instance;
}


var obj1 = new Singleton;
var obj2 = new Singleton;
Singleton.prototype.newProperty = 0;

console.log(obj1 === obj2);  // true
console.log(obj1.newProperty);  // 0
