# 接口说明
更新时间：2019-12-27

基于该接口，开发者可以轻松的获取语音合成能力
请求说明

    合成文本长度必须小于1024字节，如果本文长度较长，可以采用多次请求的方式。文本长度不可超过限制

举例，要把一段文字合成为语音文件：

result  = client.synthesis('你好百度', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

参数 	类型 	描述 	是否必须
tex 	String 	合成的文本，使用UTF-8编码，
请注意文本长度必须小于1024字节 	是
cuid 	String 	用户唯一标识，用来区分用户，
填写机器 MAC 地址或 IMEI 码，长度为60以内 	否
spd 	String 	语速，取值0-9，默认为5中语速 	否
pit 	String 	音调，取值0-9，默认为5中语调 	否
vol 	String 	音量，取值0-15，默认为5中音量 	否
per 	String 	发音人选择, 0为女声，1为男声，
3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女 	否

返回样例：

// 成功返回二进制文件流
// 失败返回
{
    "err_no":500,
    "err_msg":"notsupport.",
    "sn":"abcdefgh",
    "idx":1
}