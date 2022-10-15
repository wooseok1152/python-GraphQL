from graphene import ObjectType, String, Schema, Int, List, ID, Field

class User(ObjectType) :

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

        return User(name = name, age = age)

    def resolve_users(self, info) :

        return [
            User(name = "choi", age = 28),
            User(name = "kim", age = 30)
        ]

schema = Schema(query = Query)

result = schema.execute('''
                            query {
                                user(name : "choi", 
                                     age : 28) {
                                    name
                                    age
                                }
                                users {
                                    name
                                    age
                                }
                            }
                        ''')
print(result.data)
