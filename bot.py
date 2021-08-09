import random 
from django_tgbot.decorators import processor 
from django_tgbot.exceptions import ProcessFailure 
from django_tgbot.state_manager import state_types, update_types, message_types 
from botdevtestbot.bot import state_manager 


@processor(state_manager, from_states='', selection='any_choice', update_types=update_types.message, message_types=message_types.Text)
def choose_selection(bot, update, state)

    chat_id=update.get_chat().get_id()

    text=update.get_message().get_text()
    
    if text.lower() in ['play a game', 'anyone']:
      bot.sendMessage(chat_id, "Okay!, Select a choice ")
      {
      <form action = '???' method = "post">

      {{ formularz.as_p}}

      <input type="submit" value="Submit" />

      </form>
     
     def ShowNewses(request):

     newses = News.objects.filter(status = 'stupid')

     return render_to_response('news.html', {'news_set': newses})
     
     newses = News.objects.filter(status = 'fat')

     return render_to_response('news.html', {'news_set': newses})
     
     newses = News.objects.filter(status = 'dumb')

     return render_to_response('news.html', {'news_set': newses})
     
      state.set_memory()
      }
      return 
  else: 
      raise ProcessFailure 
@processor(state_manager, from_states='any_choice', update_types=update_types.message, message_types=message_types.Text, selection='state_types.Reset)


def choose_selection(bot, update, state)

    chat_id=update.get_chat().get_id()

    text=update.get_message().get_text()   
