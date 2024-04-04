class LLVMGenerator():
    def __init__(self, file_path: str = "./code.ll"):
        self.file_path = file_path
        self.main_text = ""
        self.tmp = 1
        self.header_text = ""

    def save(self):
        with open(self.file_path, 'w') as f:
            f.write(self.generate())

    def printf_id(self, id_: str):
        self.main_text += f"%{self.tmp} = load i32, i32* %{id_}\n"
        # self.main_text += "%"+self.tmp+" = load i32, i32* %"+id_+"\n"
        self.tmp += 1
        self.main_text += "%"+str(self.tmp) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %"+str(  # change strp to str argument for others and custom printfs
            self.tmp-1)+")\n"
        self.tmp += 1

    def scanf(self, id_: str):
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{self.id_}\n"
        self.tmp += 1

    def assign_int(self, id_: str, value: int):
        self.main_text += f"store i32 {value}, i32* %{id_}\n"

    def assign_float(self, id_: str, value: float):
        self.main_text += f"store float {value}, float* %{id_}\n"

    def assign_id_int(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_id_float(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_arr(self):
        pass

    def declare_arr(self):
        pass

    def access_arr(self):
        pass

    def declare_int(self, id_: str):
        self.main_text += f"%{id_} = alloca i32\n"

    def declare_float(self, id_: str):
        self.main_text += f"%{id_} = alloca float\n"

    def generate(self) -> str:
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += "@strstr = constant [4 x i8] c\"%s\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

    def declare_static_string(self, name: str, value: str):
        self.header_text += f"@{name} = constant [{len(value)+1} x i8] c\"{value}\\00\"\n"

    def declare_str(self, name: str):
        self.main_text += f"%{name} = alloca i8*\n"

    def allocate_str(self, name: str, length: int):
        self.main_text += f"%{name} = alloca [{length+1} x i8]\n"

    def assign_str(self, name: str):
        self.main_text += f"store i8* %{self.tmp}, i8** %{name}\n"


'''
       static void declare_string(String id){
      main_text += "%"+id+" = alloca i8*\n";
   }

   static void allocate_string(String id, int l){
      main_text += "%"+id+" = alloca ["+(l+1)+" x i8]\n";
   }

   static void assign_int(String id, String value){
      main_text += "store i32 "+value+", i32* %"+id+"\n";
   }

   static void assign_string(String id){  
      main_text += "store i8* %"+(reg-1)+", i8** %"+id+"\n";
   }

'''
