from graphene import ObjectType, String, Schema, Int, List, Field, Mutation
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.for_graphql_CRUD

class User(ObjectType) :                            

    name = String()
    age  = Int()

    def resolve_name(self, info) :

        return self.name

    def resolve_age(self, info) :

        return self.age

class Query(ObjectType) :

    user = Field(User, args = {'name' : String()})
    users = List(User)

    def resolve_user(self, info, name) :

        dict_of_user = list(db.users.find({"name" : name}, {"_id" : 0}))[0]
        return User(name = dict_of_user["name"], age = dict_of_user["age"])

    def resolve_users(self, info) :

        users = list(db.users.find({}, {"_id" : 0}))
        return [User(name = _dict["name"], age = _dict["age"]) for _dict in users]

class CreateUser(Mutation) :

    # define inputs of this mutation
    class Arguments :

        name = String()
        age  = Int()

    # field of output(output : return value for API request)
    user = Field(User)

    def mutate(self, info, name, age) :

        db.users.insert_one({"name" : name, "age" : age})
        new_user = User(name = name, age = age)
        
        return CreateUser(user = new_user)

class DeleteUser(Mutation) :

    class Arguments :

        name = String()

    user = Field(User)

    def mutate(self, info, name) :

        db.users.delete_one({"name" : name})
        deleted_user = User(name)
        
        return DeleteUser(user = deleted_user)

class Mutations(ObjectType) :

    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()

if __name__ == "__main__" :

    schema = Schema(query = Query, mutation = Mutations)

    # # Query
    # result = schema.execute('''
    #                                 {
    #                                     user(name : "choi") {
    #                                                             name
    #                                                             age
    #                                     }
    #                                 }
    #                         ''')

    # Mutation
    result = schema.execute('''
                                mutation mutations {
                                    createUser(name : "lee", age : 35) {
                                        user {
                                            name
                                            age
                                        }
                                    }
                                }
                            ''')

    print("* result :")
    print(result.data, "\n")