// import Foundation: Swift的标准库
// 这个库提供了许多基本的功能，比如字符串处理、集合、文件操作等
import Foundation

// "Hello, World!"
print("Hello, World!")

// ================ 一、变量和常量 ================
print("================ 一、变量和常量 ================")
// 声明一个变量，使用 var 关键字
var name = "John Doe"
// 声明一个常量，使用 let 关键字
let age = 30
// 打印变量和常量
print("Name: \(name), Age: \(age)")
// 修改变量的值
name = "Jane Doe"
// 打印修改后的变量
print("Updated Name: \(name)")
// 声明一个整数变量
var number: Int = 42
// 声明一个浮点数变量
var pi: Double = 3.14

// 声明一个布尔变量
var isSwiftFun: Bool = true
// 打印变量的值
print("Number: \(number), Pi: \(pi), Is Swift Fun: \(isSwiftFun)")

// 声明一个字符串变量
var greeting: String = "Hello, Swift!"
// 打印字符串变量
print(greeting)

// 声明一个数组
var fruits: [String] = ["Apple", "Banana", "Cherry"]
// 打印数组
print("Fruits: \(fruits)")

// 声明一个字典
var person: [String: Any] = ["name": "John", "age": 30, "isStudent": false]
// 打印字典
print("Person: \(person)")

// 声明一个元组
var coordinates: (x: Int, y: Int) = (10, 20)
// 打印元组
print("Coordinates: (\(coordinates.x), \(coordinates.y))")

// 声明一个可选类型
var optionalName: String? = nil
// 打印可选类型
if let name = optionalName {
    print("Optional Name: \(name)")
} else {
    print("Optional Name is nil")
}

// ================ 二、控制流 ================
print("================ 二、控制流 ================")
// 条件语句
var score = 85
if score >= 90 {
    print("Grade: A")
} else if score >= 80 {
    print("Grade: B")
} else if score >= 70 {
    print("Grade: C")
} else {
    print("Grade: D")
}
// 循环语句
for i in 1...5 {
    print("Iteration: \(i)")
}
// while 循环
var count = 0
while count < 5 {
    print("Count: \(count)")
    count += 1
}
// repeat-while 循环
count = 0
repeat {
    print("Count in repeat-while: \(count)")
    count += 1
} while count < 5
// switch 语句
let day = 3
switch day {
case 1:
    print("Monday")
case 2: 
    print("Tuesday")
case 3:
    print("Wednesday")
case 4:
    print("Thursday")
case 5:
    print("Friday")
case 6:
    print("Saturday")
case 7:
    print("Sunday")
default:
    print("Invalid day")
}

// ================ 三、函数 ================
print("================ 三、函数 ================")

// 1. 声明一个函数
func greet(name: String) -> String {
    return "Hello, \(name)!"
}
// 调用函数
let greetingMessage = greet(name: "Alice")
// 打印函数返回值
print(greetingMessage)

// 2. 声明一个带参数的函数
func add(a: Int, b: Int) -> Int {
    return a + b
}
// 调用函数
let sum = add(a: 5, b: 10)
// 打印函数返回值
print("Sum: \(sum)")

// 3. 声明一个带默认参数的函数
func multiply(a: Int, b: Int = 2) -> Int {
    return a * b
}
// 调用函数
let product1 = multiply(a: 5)
let product2 = multiply(a: 5, b: 3)
// 打印函数返回值
print("Product1: \(product1), Product2: \(product2)")

// 4. 声明一个带可变参数的函数
func sumOfNumbers(numbers: Int...) -> Int {
    var sum = 0
    for number in numbers {
        sum += number
    }
    return sum
}
// 调用函数
let total = sumOfNumbers(numbers: 1, 2, 3, 4, 5)
// 打印函数返回值
print("Total: \(total)")

// 5. 声明一个返回元组的函数
func calculate(a: Int, b: Int) -> (sum: Int, difference: Int) {
    let sum = a + b
    let difference = a - b
    return (sum, difference)
}
// 调用函数
let result = calculate(a: 10, b: 5)
// 打印函数返回值
print("Sum: \(result.sum), Difference: \(result.difference)")

// 6. 声明一个嵌套函数
func outerFunction() {
    func innerFunction() {
        print("This is an inner function.")
    }
    innerFunction()
}
// 调用嵌套函数
outerFunction()

// 7. 声明一个函数类型的变量
var operation: (Int, Int) -> Int
operation = add
// 调用函数类型的变量
let resultFromVariable = operation(10, 20)
// 打印函数类型变量的返回值
print("Result from variable: \(resultFromVariable)")

// 8. 声明一个闭包
let closure: (Int, Int) -> Int = { (a: Int, b: Int) in
    return a + b
}
// 调用闭包
let closureResult = closure(10, 20)
// 打印闭包的返回值
print("Closure Result: \(closureResult)")

// 9. 声明一个带有捕获列表的闭包
let capturedValue = 10
let capturedClosure: () -> Int = { [capturedValue] in
    return capturedValue * 2
}
// 调用带有捕获列表的闭包
let capturedClosureResult = capturedClosure()
// 打印带有捕获列表的闭包的返回值
print("Captured Closure Result: \(capturedClosureResult)")

// 10. 声明一个带有逃逸闭包的函数
// 逃逸闭包是指在函数返回后仍然可以使用的闭包
// 逃逸闭包通常用于异步操作，比如网络请求或延迟执行
// with closure: @escaping () -> Void 解释:
// @escaping 关键字表示这个闭包可能在函数返回后被调用
// () -> Void 表示这个闭包没有参数并且没有返回值
// performOperation 函数接受一个逃逸闭包作为参数
func performOperation(with closure: @escaping () -> Void) {
    // DispatchQueue.global().async 使用全局队列异步调用闭包。
    DispatchQueue.global().async {
        closure()
    }
}
// 调用带有逃逸闭包的函数
// 调用 performOperation 为什么是 {} 而不是 ()
performOperation(with: {
    print("This is an escaping closure.")
})
// 调用 performOperation 也可以使用简写的闭包语法
// 这里的 {} 是一个闭包，表示一个没有参数和返回值的函数
performOperation {
    print("This is an escaping closure.")
}

// ================ 四、类和结构体 ================
print("================ 四、类和结构体 ================")
// 1. 声明一个类
class Person {
    // 属性
    var name: String
    var age: Int
    
    // 初始化方法
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
    
    // 方法
    func introduce() -> String {
        return "My name is \(name) and I am \(age) years old."
    }
}
// 创建类的实例
let person1 = Person(name: "Alice", age: 25)
// 调用类的方法
let introduction = person1.introduce()
// 打印类的方法返回值
print(introduction)
// 2. 声明一个结构体
struct Point {
    var x: Int
    var y: Int
    
    // 方法
    func distance() -> Double {
        return sqrt(Double(x * x + y * y))
    }
}
// 创建结构体的实例
let point = Point(x: 3, y: 4)
// 调用结构体的方法
let distance = point.distance()
// 打印结构体的方法返回值
print("Distance: \(distance)")

// 类 vs 结构体
// 1. 类是引用类型，结构体是值类型
// 2. 类可以继承，结构体不能继承
// 3. 类可以有 deinit 方法，结构体没有
// 总的来说，类和结构体在 Swift 中都可以用来定义数据类型，类适合用于需要继承和引用语义的场景，
// 而结构体适合用于简单的数据封装和值语义的场景。

// 3. 类的继承
class Student: Person {
    var studentID: String
    
    init(name: String, age: Int, studentID: String) {
        self.studentID = studentID
        super.init(name: name, age: age)
    }
    
    override func introduce() -> String {
        return "My name is \(name), I am \(age) years old, and my student ID is \(studentID)."
    }
}
// 创建子类的实例
let student = Student(name: "Bob", age: 20, studentID: "S12345")
// 调用子类的方法
let studentIntroduction = student.introduce()
// 打印子类的方法返回值
print(studentIntroduction)

// 4. 类的多态
class Animal {
    func sound() -> String {
        return "Some sound"
    }
}
class Dog: Animal {
    override func sound() -> String {
        return "Woof"
    }
}
class Cat: Animal {
    override func sound() -> String {
        return "Meow"
    }
}
// 创建一个动物数组
let animals: [Animal] = [Dog(), Cat()]
// 遍历动物数组并调用 sound 方法
for animal in animals {
    print(animal.sound())
}

// 5. 类的扩展
extension Person {
    func birthday() {
        age += 1
        print("Happy Birthday! You are now \(age) years old.")
    }
}
// 调用扩展的方法
person1.birthday()
// 打印扩展的方法返回值
print("Updated Age: \(person1.age)")
// 6. 结构体的扩展
extension Point {
    func move(dx: Int, dy: Int) -> Point {
        return Point(x: x + dx, y: y + dy)
    }
}
// 调用扩展的方法
let movedPoint = point.move(dx: 1, dy: 2)
// 打印扩展的方法返回值
print("Moved Point: (\(movedPoint.x), \(movedPoint.y))")

// 7. 类的计算属性
class Circle {
    var radius: Double
    
    init(radius: Double) {
        self.radius = radius
    }
    
    // 计算属性
    var area: Double {
        return Double.pi * radius * radius
    }
}
// 创建类的实例
let circle = Circle(radius: 5)
// 打印计算属性的值
print("Circle Area: \(circle.area)")

// 8. 结构体的计算属性
struct Rectangle {
    var width: Double
    var height: Double
    
    // 计算属性
    var area: Double {
        return width * height
    }
}
// 创建结构体的实例
let rectangle = Rectangle(width: 4, height: 5)
// 打印计算属性的值
print("Rectangle Area: \(rectangle.area)")

// 9. 类的静态属性和方法
class Math {
    static let pi = 3.14159
    
    static func square(_ number: Double) -> Double {
        return number * number
    }
}
// 打印类的静态属性
print("Math Pi: \(Math.pi)")
// 调用类的静态方法
let squareResult = Math.square(5)
// 打印类的静态方法返回值
print("Square Result: \(squareResult)")

// 10. 结构体的静态属性和方法
struct Geometry {
    static let goldenRatio = 1.618033
    
    static func areaOfCircle(radius: Double) -> Double {
        return Math.pi * radius * radius
    }
}
// 打印结构体的静态属性
print("Geometry Golden Ratio: \(Geometry.goldenRatio)")
// 调用结构体的静态方法
let areaOfCircleResult = Geometry.areaOfCircle(radius: 5)
// 打印结构体的静态方法返回值
print("Area of Circle: \(areaOfCircleResult)")

// ================ 五、协议和扩展 ================
print("================ 五、协议和扩展 ================")
// 协议是 Swift 中的一种重要特性，它定义了一组方法和属性的蓝图，
// 任何类、结构体或枚举都可以遵循这些协议，从而实现协议中定义的方法和属性。
// 协议可以用于定义接口、实现多态、以及提供默认实现等。
// 扩展是 Swift 中的另一个重要特性，它允许我们为现有的类、结构体、枚举或协议添加新的功能。
// 扩展可以添加新的方法、计算属性、下标、协议遵循等。
// 1. 声明一个协议
protocol Drawable {
    func draw()
} 
// 2. 声明一个类实现协议
class DrawableCircle: Drawable {
    func draw() {
        print("Drawing a circle.")
    }
}
// 3. 声明一个结构体实现协议
struct Square: Drawable {
    func draw() {
        print("Drawing a square.")
    }
}
// 4. 声明一个枚举实现协议
enum Shape: Drawable {
    case circle
    case square
    
    func draw() {
        switch self {
        case .circle:
            print("Drawing a circle.")
        case .square:
            print("Drawing a square.")
        }
    }
}
// 5. 声明一个协议的扩展
extension Drawable {
    func drawTwice() {
        draw()
        draw()
    }
}
// 6. 调用协议的扩展方法
let circle2 = DrawableCircle()
circle2.drawTwice()
let square = Square()
square.drawTwice()
let shape = Shape.circle
shape.drawTwice()
// 7. 声明一个协议的默认实现
extension Drawable {
    func draw() {
        print("Drawing a default shape.")
    }
}
// 8. 调用协议的默认实现
let defaultShape: Drawable = Shape.square
defaultShape.draw()
// 9. 声明一个协议的继承
protocol Colorable: Drawable {
    var color: String { get }
}
// 10. 声明一个类实现继承的协议
class ColorfulCircle: Colorable {
    var color: String
    
    init(color: String) {
        self.color = color
    }
    
    func draw() {
        print("Drawing a \(color) circle.")
    }
}
// 11. 调用继承的协议的方法
let colorfulCircle = ColorfulCircle(color: "red")
colorfulCircle.draw()
// 12. 声明一个协议的关联类型
protocol Container {
    associatedtype ItemType
    var items: [ItemType] { get }
    func addItem(_ item: ItemType)
}
// 13. 声明一个类实现关联类型的协议
class StringContainer: Container {
    var items: [String] = []
    
    func addItem(_ item: String) {
        items.append(item)
    }
}
// 14. 调用关联类型的协议的方法
let stringContainer = StringContainer()
stringContainer.addItem("Hello")
stringContainer.addItem("World")
// 打印关联类型的协议的属性
print("String Container Items: \(stringContainer.items)")
// 15. 声明一个协议的组合
protocol ShapeAndColor: Drawable, Colorable { }
// 16. 声明一个类实现组合的协议
class ColorfulSquare: ShapeAndColor {
    var color: String
    
    init(color: String) {
        self.color = color
    }
    
    func draw() {
        print("Drawing a \(color) square.")
    }
}
// 17. 调用组合的协议的方法
let colorfulSquare = ColorfulSquare(color: "blue")
colorfulSquare.draw()
// 打印组合的协议的属性
print("Colorful Square Color: \(colorfulSquare.color)")
// 18. 声明一个协议的泛型
protocol GenericContainer {
    associatedtype ItemType
    var items: [ItemType] { get }
    func addItem(_ item: ItemType)
}
// 19. 声明一个类实现泛型的协议
class IntContainer: GenericContainer {
    var items: [Int] = []
    
    func addItem(_ item: Int) {
        items.append(item)
    }
}
// 20. 调用泛型的协议的方法
let intContainer = IntContainer()
intContainer.addItem(1)
intContainer.addItem(2)
// 打印泛型的协议的属性
print("Int Container Items: \(intContainer.items)")
// 21. 声明一个协议的嵌套类型
protocol NestedTypeProtocol {
    associatedtype NestedType
    var nestedValue: NestedType { get }
}
// 22. 声明一个类实现嵌套类型的协议
class NestedTypeClass: NestedTypeProtocol {
    typealias NestedType = String
    var nestedValue: String {
        return "Nested Value"
    }
}
// 23. 调用嵌套类型的协议的方法
let nestedTypeInstance = NestedTypeClass()
// 打印嵌套类型的协议的属性
print("Nested Type Value: \(nestedTypeInstance.nestedValue)")

// ================ 六、错误处理 ================
print("================ 六、错误处理 ================")
// 错误处理是 Swift 中的一种重要特性，它允许我们处理运行时错误。
// Swift 提供了多种错误处理机制，包括抛出错误、捕获错误、以及使用 do-catch 语句。
// 1. 声明一个错误类型
enum MathError: Error {
    case divisionByZero
    case negativeSquareRoot
}
// 2. 声明一个函数抛出错误
func divide(_ a: Double, by b: Double) throws -> Double {
    if b == 0 {
        throw MathError.divisionByZero
    }
    return a / b
}
// 3. 调用抛出错误的函数
do {
    let result = try divide(10, by: 0)
    print("Result: \(result)")
} catch MathError.divisionByZero {
    print("Error: Division by zero.")
} catch {
    print("Error: \(error)")
}
