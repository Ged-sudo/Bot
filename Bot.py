import settings
import telebot
from telebot import types

bot = telebot.TeleBot(settings.TOKEN)
markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
item_id = types.KeyboardButton("Перейти в меню")

Ssilka = types.InlineKeyboardMarkup()

GosAkStep = types.InlineKeyboardButton(text=
                                                 "Государственная академическая стипендия",
                                                 callback_data = 'GosAkStep')
GosSocStep = types.InlineKeyboardButton(text =
                                                  "Государственная социальная стипендия",
                                                  callback_data = "GosSocStep")
RazmStep = types.InlineKeyboardButton(text =
                                                "Размеры стипендий",
                                                callback_data = "RazmStep")


Ssilka.row(GosSocStep)
Ssilka.row(GosAkStep)
Ssilka.row(RazmStep)

@bot.message_handler(commands = ["start"])
def start(message):

     menueButton = types.KeyboardButton("Перейти в меню")
     MenueMarkup = types.ReplyKeyboardMarkup(resize_keyboard = True)
     MenueMarkup.add(menueButton)

     bot.send_message(message.chat.id,
                      'Привет, студент! Это бот Профкома студентов и аспирантов МГУ им. Н.П. Огарёва. Здесь ты можешь найти ответы на часто задаваемые вопросы. Если же их не оказалось, то пиши в сообщения нашей группы https://vk.com/profkom_mrsu.',
                      reply_markup = MenueMarkup)

@bot.message_handler(content_types = ["text"])
def menue(mes):
     if mes.text == "Перейти в меню":
          MenueInLine = types.InlineKeyboardMarkup()

          Snatoriy = types.InlineKeyboardButton(text =
                                                "Санаторий-профилакторий",
                                                callback_data = 'Sanatoriy')
          MatHelp = types.InlineKeyboardButton(text =
                                               "Материальная помощь",
                                               callback_data = 'MatHelp')
          HowIncludeProf = types.InlineKeyboardButton(text =
                                                      "Как вступить в Профсоюз",
                                                      callback_data = 'HowIncludeProf')
          Stependiya = types.InlineKeyboardButton(text =
                                                  "Стипендии",

                                                  callback_data = 'Stependiya')
          LgotnProezdnoy = types.InlineKeyboardButton(text =
                                                      "Льготный проездной",
                                                      callback_data = 'LgotnProezdoy')


          MenueInLine.row(HowIncludeProf)
          MenueInLine.row(MatHelp)
          MenueInLine.row(LgotnProezdnoy)
          MenueInLine.row(Stependiya)
          MenueInLine.row(Snatoriy)
          bot.send_message(mes.chat.id,
                           "Наше меню представлено ниже",
                           reply_markup = MenueInLine)

@bot.callback_query_handler(func = lambda call: True)
def res(call):
     if call.data == 'HowIncludeProf':
          markup_reply.add(item_id)
          bot.send_message(call.message.chat.id,
                           '1. Прийти в Профком (АБК, каб. №210) или к председателю профсоюзного бюро своего факультета;\n2. Заполнить заявление на вступление в Профсоюз и удержание профсоюзных взносов;\n3. Получить профсоюзный билет.Поздравляем! Ты в нашей команде!')

          bot.send_message(call.message.chat.id, 'При вступлении в Профсоюз появляется много возможностей: \n- твои права будут защищены;\n- сможешь оформить материальную помощь; \n- покупать билеты в вагонах купе со скидкой 25% от РЖД-бонус; \n- участвовать в крупных культурно-массовых и спортивных мероприятиях; \n- получить путевку на летний отдых; \n- бесплатно оздоравливаться в санатории-профилактории.')

     if call.data == 'Stependiya':



          bot.send_message(call.message.chat.id,
                           "Стипендии",
                           reply_markup = Ssilka)


     if call.data == 'Sanatoriy':
          bot.send_message(call.message.chat.id,
                           "Как заселиться:\n– взять заявление в профбюро своего факультета/института;\n– заполнить заявление и заверить подписью и печатью деканата или дирекции;\n– сходить в поликлинику (для иногородних студентов - поликлиника №3, для местных – по месту жительства) к терапевту, для того, чтобы Вам выдали справку для получения путевки;\n– прийти в Профком студентов и аспирантов за путевкой (АБК, 210 каб);\n– получить санаторно-курортную карту у терапевта;\n– заселиться в профилакторий.")
          bot.send_message(call.message.chat.id,
                           "Для получения путевки необходимы следующие документы:\n- справка на получение путевки от терапевта;\n- заявление с печатью, подписанное заместителем директора института по внеучебной работе;\n- паспорт, профсоюзный билет, студенческий билет;\n- сертификат о вакцинации от COVID-19;\n- 1 фотография 3х4.")

          file = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Заявление Санаторий.doc", "rb")
          bot.send_document(call.message.chat.id, file)
          fileEx = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Пример по заполнению мат. помощь.docx", "rb")
          bot.send_document(call.message.chat.id, fileEx)


     if call.data == 'MatHelp':
          bot.send_message(call.message.chat.id,
                           "как получить материальную помощь:")
          bot.send_message(call.message.chat.id,
                           "- взять заявление у председателя профсоюзного бюро своего факультета/института\n- заполнить заявление и приложить копии документов, в соответствии с основанием оказания материальной помощи.")

          file = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Материальная помощь.docx", "rb")
          bot.send_document(call.message.chat.id,  file)
          fileHelp = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Пример по заполнению.docx", "rb")
          bot.send_document(call.message.chat.id, fileHelp)
          fileEx = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Razmery_Materialnoy_Pomoschi_Obuchayuschimsya.docx", "rb")
          bot.send_document(call.message.chat.id, fileEx)


     if call.data == 'LgotnProezdoy':
          UrlMenue = types.InlineKeyboardMarkup()
          StepURL = types.InlineKeyboardButton(text =
                                               "Ссылка на нужный материал",
                                               url =
                                               'https://docs.cntd.ru/document/450221146?marker')
          UrlMenue.add(StepURL)
          bot.send_message(call.message.chat.id,
                           "Список категорий студентов, которые могут иметь льготный проездной:\n- студенты, имеющие гражданство Российской Федерации, относящиеся к категориям, в постановлении Правительства Республики Мордовия от 30.08.2021 г. № 402 «О внесении изменений в пункт 2.2. постановления Правительства Республики Мордовия от 19 мая 2017 г. № 315»;\n- студенты и аспиранты очной формы обучения, имеющие гражданство Российской Федерации, первого курса и первого года обучения из малоимущих семей.")
          bot.send_message(call.message.chat.id,
                           "Список документов, необходимых для получения проездного:\n- справка о составе семьи;\n- справка о доходах на каждого члена семьи;\n- справка с места учебы о том, что заявитель является студентом, аспирантом очной формы обучения, студенческий билет студентам и аспирантский билет аспирантам.")




     if call.data == 'RazmStep':
          fileRS = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Razmery_Stipendy_S_01_09_21.docx", "rb")
          bot.send_document(call.message.chat.id, fileRS)
          pass

     if call.data == 'GosSocStep':
          Mun = types.InlineKeyboardMarkup()
          KtoMozhPret = types.InlineKeyboardButton(text =
                                                   "Кто может претендовать на соц. стипендию",
                                                   callback_data = "KtoMozhPretStep")
          DocumentsSoc = types.InlineKeyboardButton(text =
                                                    "Документы для оформления соц.стипендии",
                                                   callback_data = "DocumentsSoc")
          AspirOrd = types.InlineKeyboardButton(text=
                                                "Имеют ли право аспиранты, ординаторы на соц. стипендию?",
                                                   callback_data = "AspOrd")

          Mun.row(KtoMozhPret)
          Mun.row(DocumentsSoc)
          Mun.row(AspirOrd)

          bot.send_message(call.message.chat.id, "Стипендии", reply_markup = Mun)


     if call.data == 'GosAkStep':
          bot.send_message(call.message.chat.id,
                           "Требования для получения стипендии:\n1. Отсутствие по итогам промежуточной аттестации оценки «удовлетворительно»;\n2. Отсутствие академической задолженности.")
          bot.send_message(call.message.chat.id,
                           "Прекращение выплаты:\n- с момента отчисления из организации (пропорционально дням с первого числа месяца до даты отчисления);\n- с первого числа месяца, следующего за месяцем получения студентом оценки 'удовлетворительно' во время прохождения промежуточной аттестации;\n- с первого числа месяца, следующего за месяцем образования у студента академической задолженности.", reply_markup=Ssilka)



     if call.data == "KtoMozhPretStep":
          bot.send_message(call.message.chat.id, "- дети-сироты и деты, оставшиеся без попечения родителей, лица из числа детей-сирот и детей, оставшихся без попечения родителей;\n- лица, потерявшие в период обучения обоих родителей или единственного родителя;\n- дети-инвалиды, инвалиды I и II групп, инвалиды с детства;\n- студенты, подвергшиеся воздействию радиации вследствие катастрофы на Чернобыльской АЭС и иных радиационных катастроф, вследствие ядерных испытаний на Семипалатинском полигоне;\n- ветераны боевых действий, а также студенты из числа граждан, проходившие в течение 3-х лет и более службу по контракту;\n- студенты, являющиеся инвалидами, вследствие получения травмы или заболевания в период похождения военной службы;\n- студенты, получающие государственную социальную помощь.", reply_markup=Ssilka)


     if call.data == "DocumentsSoc":
          fileSoc = open("/Users/evgenijandronov/Documents/Профсоюзный бот/Sotsialnaya_Stipendia.pdf", "rb")
          bot.send_document(call.message.chat.id, fileSoc)


     if call.data == "AspOrd":
          bot.send_message(call.message.chat.id, "Имеют ли право аспиранты, ординаторы на соц. стипендию?\n\nНет, такая выплата есть только у студентов")






if __name__ == '__main__':
     bot.polling(none_stop=True)