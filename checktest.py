import re
from datetime import datetime
import asyncio
error = f"❗️ Xato tartibda kiritdiz!\n" \
                  f"##testkodi##to'g'rijavoblar\n" \
                  f"Misol:\n" \
                  f"##2056##1A2B3C4D5A6B...\n" \
                  f"❗️ <b>Boshqa ko'rinishlar xato hisoblanadi.Iltimos diqqatli bo'ling!</b>"
async def gototrueformat(answers):
    keys = re.findall(r'\d+', answers)
    values = re.findall(r'[a-zA-Z]', answers)
    values = [x.upper() for x in values]
    results = {str(keys[i]): values[i] for i in range(len(keys))}
    return results
async def checkformat(answers:str):
    if answers.startswith('##'):
        
            try:
                cut = answers.rfind('##')
                javoblar = answers[cut:]
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                if len(keys) == len(values):
                    data = {}
                    data['answers'] = await gototrueformat(answers=javoblar)
                    data['answers_string'] =javoblar
                    data['len'] = len(await gototrueformat(answers=javoblar))
                    return data
                else:
                    return False
            except:
                return False
       
    else:
        return False
async def checkformatschool(answers:str):
    if answers.startswith('@@'):  
            try:
                cut = answers.rfind('@@') + 2
                print(cut)
                javoblar = answers[cut:]
                print(javoblar)
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                print(keys,values)
                if len(keys) == len(values):
                    data = {}
                    data['test_code'] =answers[2:answers.rfind('@@')]
                    data['answers'] = await gototrueformat(answers=javoblar)
                    data['answers_string'] =javoblar
                    data['len'] = len(await gototrueformat(answers=javoblar))
                    return data
                else:
                    return False
            except Exception as e:
                print(e)
                return False
       
    else:
        return False
async def checkformat_1(answers:str):
    if answers.startswith('++'):
        if answers.count('+')==4:
            try:
                cut = answers.rfind('++') + 2
                javoblar = answers[cut:]
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                if len(keys) == len(values):
                    data = {}
                    data['test_code'] =answers[2:answers.rfind('++')]
                    data['answers'] = await gototrueformat(answers=javoblar)
                    data['answers_string'] =javoblar
                    data['len'] = len(await gototrueformat(answers=javoblar))
                    return data
                else:
                    return False
            except:
                return False
        else:
            return False
    else:
        return False
async def checkformat_3(answers:str):
   
    if answers.startswith('!!'):
       
        if answers.count('!')==4:
           
            try:
                cut = answers.rfind('!!') + 2
                javoblar = answers[cut:]
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                if len(keys) == len(values):
                   
                    data = {}
                    data['test_code'] =answers[2:answers.rfind('!!')]
                    data['answers'] = await gototrueformat(answers=javoblar)
                    data['answers_string'] =javoblar
                    data['len'] = len(await gototrueformat(answers=javoblar))
                    return data
                else:
                    return False
            except:
                return False
        else:
            return False
    else:
        return False
async def check_answers(trueanswers,answers):
    text = ''
    tr=0
    fl = 0
    med  = []
    for i in trueanswers:
        if trueanswers.get(i) == answers.get(i):
            tr+=1
            med.append(f'{i}.{trueanswers.get(i)} ✅')
        else:
            fl+=1  
            med.append(f'{i}.{trueanswers.get(i)} ❌')        
    all = tr+fl
    score = tr*100 / all
    level = ''
    print(med)
    lines = []
    text_=''
    for i in range(0, len(med),3):
        row = med[i:i+3]
        text_+="\t\t\t".join("{}".format(x) for x in row)+'\n'
    toifa = ''
    if score >60 and score<70:
        level ="Tabriklaymiz, siz 2-toifaga o‘tdingiz!"
        toifa = '2-toifa'
    elif score >70 and score <80:
        level = "Tabriklaymiz, siz 1-toifaga o‘tdingiz!"
        toifa = '1-toifa'
    elif score >86:
        level = "Tabriklaymiz, siz oliy toifaga o‘tdingiz va 70% ustamani qo‘lga kiritdingiz!"
        toifa = 'Oliy toifa'
    else:
        level = "Testdan o'tolmadingiz!"
        toifa= ''
    score = "{:.2f}".format(score)
    
    now = datetime.now()
    now_date = now.strftime("%m.%d.%Y")
    now_hour = now.strftime("%H:%M:%S")
    text+=(f"✅ To'g'ri javoblar: <b>{tr}</b> ta\n"
          f"❌ Xato javoblar: <b>{fl}</b> ta\n"
          f"🎯 Sifat ko'rsatkichi: <b>{score}</b> %\n\n"
          f"🗓️ {now_date} ⏱️ {now_hour}\n\n"
           f"✅ Attestatsiya testi")
    data = {}
    data['result'] = text
    data['trues'] = tr
    data['falses']  = fl
    data['score'] = score
    data['level']=level
    data['text_']=text_
    data['toifa']=toifa
    return data

async def checkformat_2(javoblar:str):
        try:
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                if len(keys) == len(values):
                    data = {}
                    data['answers'] = await gototrueformat(answers=javoblar)
                    return data['answers']
                else:
                    return False
        except:
                return False
async def show_answers(data):
    items = list(data.items())
    text =''
    for i in range(0, len(items), 5):
        row = items[i:i+5]
        text+="  ".join(f"{k}.{v}" for k, v in row)+'\n'
    return text
async def info_degree_(all,trues):
    score = trues*100 / all
    toifa = ''
    if score >60 and score<70:
      
        toifa = '2-toifa'
    elif score >70 and score <80:
      
        toifa = '1-toifa'
    elif score >86:
       
        toifa = 'Oliy toifa'
    else:
        level = "Testdan o'tolmadingiz!"
        toifa= ''
    return toifa

async def check_answers_2(trueanswers,answers):
    text = ''
    tr=0
    fl = 0
    med  = []
    for i in trueanswers:
        if trueanswers.get(i) == answers.get(i):
            tr+=1
            med.append(f'{i}.{trueanswers.get(i)} ✅')
        else:
            fl+=1  
            med.append(f'{i}.{trueanswers.get(i)} ❌')        
    all = tr+fl
    score = tr*100 / all
    level = ''
    print(med)
    lines = []
    text_=''
    for i in range(0, len(med),3):
        row = med[i:i+3]
        text_+="\t\t\t".join("{}".format(x) for x in row)+'\n'
    
    score = "{:.2f}".format(score)
    toifa = f"🎯 Siz testdan {score} % lik natijani qo'lgan kiritdiz"
    now = datetime.now()
    now_date = now.strftime("%m.%d.%Y")
    now_hour = now.strftime("%H:%M:%S")
    text+=(f"✅ To'g'ri javoblar: <b>{tr}</b> ta\n"
          f"❌ Xato javoblar: <b>{fl}</b> ta\n"
          f"🎯 Sifat ko'rsatkichi: <b>{score}</b> %\n\n"
           f"🗓️ {now_date} ⏱️ {now_hour}\n\n"
           f"✅ Maktab testi")
    data = {}
    data['result'] = text
    data['trues'] = tr
    data['falses']  = fl
    data['score'] = score
    data['level']=level
    data['text_']=text_
    data['toifa']=toifa
    return data


import re
def parse_data(text: str):
    pattern = r"\=\=(.*?)\=\=(.*?)\=\=(.*)"
    match = re.match(pattern, text)
    
    if match:
        return True
    else:
        return False
def parse_format(text: str):
    parts = text.split("==")
    # split result: ['', 'class_number', 'subject', '1a2b3c4d']
    
    if len(parts) >= 4:
        class_number = parts[1]
        subject = parts[2]
        answers = parts[3]
        return [class_number, subject, answers]
    
    return []
async def checkformat_school(answers:str):
    if answers.startswith('=='):
        if answers.count('=')==6:
            try:
                if parse_data(answers):
                    data_me = parse_format(answers)
                    if data_me==[]:
                        pass
                    else:
                        javoblar = data_me[2]
                        keys = re.findall(r'\d+', javoblar)
                        values = re.findall(r'[a-zA-Z]', javoblar)
                        if len(keys) == len(values):
                            data = {}
                            data['class_number'] =data_me[0]
                            data['subject'] = data_me[1]
                            data['answers'] = await gototrueformat(answers=javoblar)
                            data['answers_string'] =javoblar
                            data['len'] = len(await gototrueformat(answers=javoblar))
                            return data
                        else:
                            return False
                else:
                    return False
            except Exception as e:
               
                return False
        else:
            return False
    else:
        return False
async def checkformat_2305(answers:str):
   
    if answers.startswith('%%'):
       
        if answers.count('%')==4:
           
            try:
                cut = answers.rfind('%%') + 2
                javoblar = answers[cut:]
                keys = re.findall(r'\d+', javoblar)
                values = re.findall(r'[a-zA-Z]', javoblar)
                if len(keys) == len(values):
                   
                    data = {}
                    data['test_code'] =answers[2:answers.rfind('%%')]
                    data['answers'] = await gototrueformat(answers=javoblar)
                    data['answers_string'] =javoblar
                    data['len'] = len(await gototrueformat(answers=javoblar))
                    return data
                else:
                    return False
            except:
                return False
        else:
            return False
    else:
        return False
if __name__ =='__main__':
    print(asyncio.run(checkformatschool('@@a12b3d')))