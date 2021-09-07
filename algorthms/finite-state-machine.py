from enum import Enum

def isAddress(address: str) -> bool:

    #定义状态
    State = Enum("State", [
        "STATE_INITIAL", #开始
        "STATE_PROVINCE", # 省
        "STATE_CITY", # 市
        "STATE_AREA", # 区 / 县
        "STATE_STREET", # 街道
        "STATE_NUM", #号
        "STATE_END", #结束
        "STATE_ILLEGAL", #错误状态
    ])

    def toAddressType(addr_slice : str) -> State:
        if "省" in addr_slice:
            return State.STATE_PROVINCE
        elif "市" in addr_slice:
            return State.STATE_CITY
        elif "区" in addr_slice or "县" in addr_slice:
            return State.STATE_AREA
        elif "路" in addr_slice or "街道" in addr_slice:
            return State.STATE_STREET
        elif "号" in addr_slice:
            return State.STATE_NUM
        else:
            return State.STATE_ILLEGAL
    
    #定义状态转移
    
    transfer = {

        #开始可以转为 省或市
        State.STATE_INITIAL: {
            State.STATE_PROVINCE, 
            State.STATE_CITY,
        },

        #省可以转 市或区县
        State.STATE_PROVINCE:{
            State.STATE_CITY,
            State.STATE_AREA,
        },

        #市可以转区或街道
        State.STATE_CITY: {
            State.STATE_AREA,
            State.STATE_STREET,
        },

        #区县可以转街道
        State.STATE_AREA: {
            State.STATE_STREET,
        },

        #街道可以转号或终止
        State.STATE_STREET: {
            State.STATE_NUM,
            State.STATE_END,
        },

        #号只能转终止
        State.STATE_NUM: {
            State.STATE_END,
        },
    }

    st = State.STATE_INITIAL
    for ch in address:
        current_state = toAddressType(ch)
        if current_state not in transfer[st]:
            return False
        st = current_state 

    return st in [State.STATE_STREET, State.STATE_NUM,State.STATE_END]

if __name__ == '__main__':
    address1 = ["江苏省","苏州市", "吴中区", "中山北路", "208号"]
    address2 = ["苏州市","吴中区", "中山北路", "208号"]
    address3 = ["苏州市","吴江区", "中山北路", "208号"]
    address4 = ["苏州市","吴江区","208号"]
    address5 = ["苏州市","中山北路"]
    address6 = ["苏州市","江苏省","中山北路"]

    assert isAddress(address1)
    assert isAddress(address2)
    assert isAddress(address3)
    assert isAddress(address5)
    assert isAddress(address4) == False
    assert isAddress(address6) == False