import threading
import ali_speech
# from ali_speech.callbacks import SpeechSynthesizerCallback
# from ali_speech.constant import TTSFormat
# from ali_speech.constant import TTSSampleRate
class MyCallback(SpeechSynthesizerCallback):
    def __init__(self, name):
        self._name = name
        self._fout = open(name, 'wb')
    def on_binary_data_received(self, raw):
        print('MyCallback.on_binary_data_received: %s' % len(raw))
        self._fout.write(raw)
    def on_completed(self, message):
        print('MyCallback.OnRecognitionCompleted: %s' % message)
        self._fout.close()
    def on_task_failed(self, message):
        print('MyCallback.OnRecognitionTaskFailed-task_id:%s, status_text:%s' % (
            message['header']['task_id'], message['header']['status_text']))
        self._fout.close()
    def on_channel_closed(self):
        print('MyCallback.OnRecognitionChannelClosed')
def process(client, appkey, token, text, audio_name):
    callback = MyCallback(audio_name)
    synthesizer = client.create_synthesizer(callback)
    synthesizer.set_appkey(appkey)
    synthesizer.set_token(token)
    synthesizer.set_voice('xiaoyun')
    synthesizer.set_text(text)
    synthesizer.set_format(TTSFormat.WAV)
    synthesizer.set_sample_rate(TTSSampleRate.SAMPLE_RATE_16K)
    synthesizer.set_volume(50)
    synthesizer.set_speech_rate(0)
    synthesizer.set_pitch_rate(0)
    try:
        ret = synthesizer.start()
        if ret < 0:
            return ret
        synthesizer.wait_completed()
    except Exception as e:
        print(e)
    finally:
        synthesizer.close()
def process_multithread(client, appkey, token, number):
    thread_list = []
    for i in range(0, number):
        text = "" + str(i) + ""
        audio_name = "sy_audio_" + str(i) + ".wav"
        thread = threading.Thread(target=process, args=(client, appkey, token, text, audio_name))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
if __name__ == "__main__":
    client = ali_speech.NlsClient()
    client.set_log_level('INFO')
    appkey = 'Hij5upBkMQiHVgcU'
    token = '2100c80453e94c8188e9453e4773000e'
    text = ""
    audio_name = 'sy_audio.wav'
    process(client, appkey, token, text, audio_name)
    # process_multithread(client, appkey, token, 2)