// 实现一个单例类singleton 懒汉模式

#include <iostream>
using namespace std;

class singleton
{
public:
    static singleton* getInstance()
    {
        if (instance == NULL)
        {
            instance = new singleton();
        }
        return instance;
    }
private:
    singleton() {}
    static singleton* instance;
};

// 根据以上代码生成一个UML类图，如下图所示：
// 由于instance是静态成员，所以它在类的所有对象中是共享的，也就是说，所有的对象都指向同一个instance。
// 但是，由于instance是私有的，所以只能通过getInstance()来访问它，这样就保证了只有一个instance被创建。
// 但是，这样的实现方式有一个问题，就是当getInstance()被多个线程同时调用时，可能会创建多个instance。
// 为了解决这个问题，我们可以在getInstance()前面加上synchronized关键字，如下所示：
