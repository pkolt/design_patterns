/*
* Наблюдатель (Observer, Dependents, Publish-Subscribe) - паттерн поведения объектов.
*
* Определяет зависимость типа "один ко многим" между объектами таким образом,
* что при изменении состояния одного объекта все зависящие от него оповещаются об этом
* и автоматически обновляются.
*
* */


function Subject(){
    /* Субъект */
    this.data = null;
    this.observers = [];
}

Subject.prototype.attach = function(observer){
    /* подписаться на оповещение */

    // проверим класс добавляемого объекта
    if (!observer instanceof Observer){
        throw Error('Неверный класс объекта');
    }

    for(var i = 0; i < this.observers.length; i++){
        if(this.observers[i] === observer){
            return;
        }
    }
    this.observers.push(observer);
};

Subject.prototype.detach = function(observer){
    /* отписаться от оповещения */
    for(var i = 0; i < this.observers.length; i++){
        if(this.observers[i] === observer){
            this.observers.splice(i, 1);
            return;
        }
    }
};

Subject.prototype.getData = function(){
    return this.data;
};

Subject.prototype.setData = function(data){
    this.data = data;
    this.notify(data);
};

Subject.prototype.notify = function(data){
    /* уведомить всех наблюдателей о событии */
    for(var i = 0; i < this.observers.length; i++){
        this.observers[i].update(data);
    }
};

function Observer(name){
    /* Наблюдатель */
    this.name = name;
}

Observer.prototype.update = function(data){
    console.log(this.name, ':', data);
};

var subject = new Subject(),
    observer1 = new Observer('Наблюдатель 1'),
    observer2 = new Observer('Наблюдатель 2');

subject.attach(observer1);
subject.attach(observer2);
subject.setData('данные для наблюдателя');

// Наблюдатель 1 : данные для наблюдателя
// Наблюдатель 2 : данные для наблюдателя