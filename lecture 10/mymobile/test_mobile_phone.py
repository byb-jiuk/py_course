from mobile_phone_class import MobilePhone



def test_turn_on():
    phone = MobilePhone(3752900770007)
    assert not phone.switch  # Проверяем, что телефон изначально выключен
    message = phone.turn_on()
    assert phone.switch  # Проверяем, что телефон включен после вызова turn_on
    assert message == 'mobile phone 3752900770007 is turned on'

def test_call_when_off():
    phone = MobilePhone(375330011001)
    message = phone.call("2889933")
    assert message == "Mobile phone is turned off. Can't make a call."
