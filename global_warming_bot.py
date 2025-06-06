import logging
import telebot

API_TOKEN = '8000101066:AAHgDYk02TT0YE1wgvajXstlFKht3dVaRKFCs'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание экземпляра бота
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот, который расскажет о глобальном потеплении. '
                          'Используйте команды: /info, /seriousness, /solutions, /factors.😁')

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, 'Глобальное потепление — распространенное название изменения климата, которое идет уже около двух веков.'
                          ' ООН определяет это явление как долгосрочные изменения температуры и погодных условий, вызванное естественными причинами, вроде активности Солнца, и антропогенными — из-за действий человека😥')

@bot.message_handler(commands=['seriousness'])
def seriousness(message):
    bot.reply_to(message, 'Глобальное потепление — серьёзная проблема, которая может привести к значительным последствиям для Земли и человека.'
                        'Некоторые из них:'

                        'Повышение уровня моря. К концу XXI века он может подняться на 52–98 см. Это вызвано расширением тёплой воды и таянием ледников. Следствием станет потеря мест обитания людей.'
                        'Участившиеся экстремальные погодные явления. К ним относятся ураганы, ливни, наводнения, засухи и пересыхание рек.'
                        'Вымирание биологических видов. Особенно страдают обитатели прибрежных зон и островов.' 
                        'Угроза продовольственной безопасности. Она вызвана неурожаями при потеплении.' 
                        'Ухудшение условий жизни. Из-за катаклизмов, возникающих на фоне изменения климата, многие люди могут лишиться крова.'
                        'Влияние на здоровье людей. Повышение температур и высокие содержания в атмосфере загрязняющих веществ ведут к обострению сердечно-сосудистых и лёгочных заболеваний.'
                        'Межправительственная группа экспертов по изменению климата при ООН (МГЭИК) прогнозирует глобальное повышение температуры на 1,5 градуса к 2030 году.'

                        'Главной причиной глобального потепления называют деятельность человека, в частности выбросы парниковых газов.💀')

@bot.message_handler(commands=['solutions'])
def solutions(message):
    bot.reply_to(message, 'Способы борьбы с глобальным потеплением включают:'
                        '\n1. Уменьшение выбросов парниковых газов: Сокращение использования ископаемого топлива: Переход на более чистые источники энергии, такие как солнечная, ветровая и гидроэнергетика. Улучшение технологий: Разработка и внедрение более чистых технологий в промышленности и транспорте.'
                          
                        '\n2. Повышение энергоэффективности: Энергоэффективные здания: Использование изоляционных материалов, энергоэффективных окон и систем отопления/охлаждения. Энергоэффективные приборы: Замена старых бытовых приборов на более экономичные.'
                          
                        '\n3. Переход на возобновляемые источники энергии: Солнечные панели: Установка солнечных батарей для выработки электроэнергии.'

                        '\n4. Ветровые установки: Использование ветровой энергии для производства электричества.'
                          
                        '\n5. Изменение образа жизни'
                        
                        '\n6.Сокращение потребления мяса: Переход на растительную диету или уменьшение потребления мяса, что снижает выбросы метана от скота.'

                        '\n7. Использование общественного транспорта: Снижение использования личных автомобилей в пользу общественного транспорта, велосипедов или пеших прогулок.')
                          
                        
                        
                        
@bot.message_handler(commands=['factors'])
def factors(message):
    bot.reply_to(message, 'Ключевые факторы прогрессии глобального потепления:'
                          '\n1. Выбросы парниковых газов: Основной причиной глобального потепления являются выбросы углекислого газа (CO2), метана (CH4), закиси азота (N2O) и других парниковых газов в атмосферу. Эти газы задерживают тепло, что приводит к повышению температуры на планете.'
                          '\n2. Сжигание ископаемого топлива: Использование угля, нефти и природного газа для производства энергии и транспорта является основным источником CO2.'
                          '\n3. Обезлесение: Вырубка лесов для сельского хозяйства, строительства и других нужд уменьшает количество деревьев, которые поглощают CO2, что усугубляет проблему.'
                          '\n4. Сельское хозяйство: Сельское хозяйство, особенно животноводство, производит значительные объемы метана и закиси азота. Метан выделяется при переваривании пищи у животных и разложении органических веществ.')

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
