from graphene import ObjectType, String, Schema, Int, List, ID, Field

class User(ObjectType) :                            # 'ObjectType'클래스를 상속했기 때문에, ObjectType 클래스의 생성자 함수도 상속됨

    name = String()
    age  = Int()

    def resolve_name(self, info) :

        return self.name

    def resolve_age(self, info) :

        return self.age

class Query(ObjectType) :

    user = Field(User, args = {'name' : String(), 'age' : Int()})
    users = List(User)

    def resolve_user(self, info, name, age) :

        return User(name = name, age = age)         # 'ObjectType'클래스의 생성자 함수가 호출됨

    def resolve_users(self, info) :

        return [
            User(name = "choi", age = 28),
            User(name = "kim", age = 30)
        ]

schema = Schema(query = Query)

result = schema.execute('''
                            query {
                                user(name : "choi", age : 28) {
                                                                name
                                                                age
                                                              }
                                users {
                                    name
                                    age
                                }
                            }
                        ''')                        # 'user'에 대한 쿼리 요청시, 두 개의 인자(name, age)를 입력함
print(result.data)
