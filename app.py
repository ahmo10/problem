from flask import Flask,jsonify
from flask_restplus import Resource, Api,fields,Namespace


app = create_app('development')
api = Api(prefix='/api/v1')
entries = Namespace('entries', description="Diary entries")
my_diary=api.model("Diary",{
                            "date": fields.Integer(readOnly=True, description="Diary date created"),
                            "title":fields.String("Title of the diary"),
                            "Description":fields.String("The body of the diary")})

data=[]

class Entry:
    entry_id=0
    def __init__(self,date,title,description):
        global data
        self.date=date
        self.title=title
        self.description=description
    def create_diary(self):
        create_diary = {
            "Date": self.date,
            "Title": self.title,
            "description": self.description
        }
        Entry.entry_id += 1
        final_data = data.append(create_diary)
        return  final_data

class diaryApp(object):
    def __init__(self):
        self.counter = 0
        self.datadata = []

    def get_all_entries(self):
        return self.datadata

    def create(self, data):
        entry = data
        entry['id'] = self.counter = self.counter + 1
        self.datadata.append(entry)
        return entry
    def get_one_entry(self, id):
        for entry in self.datadata:
            if entry['id'] == id:
                return entry
    def update(self, id, data):
        entry = self.get_one_entry(id)
        entry.update(data)
        return entry

    def delete(self, id):
        entry = self.get_one_entry(id)
        self.datadata.remove(entry)
    

data2 = diaryApp()

class myDiary(Resource):
    def get(self):
        return data2.get_all_entries(),
    @entries.expect(my_diary)
    def post(self):
        return data2.create(api.payload), 201
entries.add_resource(myDiary, '')

class myDiary_id(Resource):
    def get(self, id):
        
        return data2.get_one_entry(id)
    def delete(self, id):
        
        data2.delete(id)
        return '', 204

    @entries.expect(my_diary)
    def put(self, id):
        return data2.update(id, api.payload),201

entries.add_resource(myDiary_id, '/<int:id>')
api.add_namespace(entries)

api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)