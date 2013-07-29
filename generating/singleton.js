
function Singleton(name){
    if (typeof Singleton.instance === 'object'){
        return Singleton.instance;
    }
    this.name = name;
    Singleton.instance = this;
    return this;
}

Singleton.prototype.getName = function(){
    return this.name;
};

var obj1 = new Singleton('MyInstance 1');
console.log(obj1.getName()); // MyInstance 1

var obj2 = new Singleton('MyInstance 2');
console.log(obj2.getName()); // MyInstance 1

console.log(obj1 === obj2); // True