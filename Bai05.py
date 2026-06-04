""" 
    HÀM find_patient_id_patient_list()
    INPUT: DANH SÁCH, ID MUỐN TÌM
    OUTPUT: GIÁ TRỊ CHỈ SỐ TRONG MẢNG HOẶC -1
    HÀM check_is_empty()
    INPUT:DANH SÁCH BỆNH NHÂN
    OUTPUT: TRUE OR FALSE 

   BẪY 1: NHẬP TRÙNG MÃ CA CẤP CỨU TA SỬU DỤNG CHECK LẠI VỚI HÀM
   BẪY 2: NHẬP TRÙNG MÃ BỆNH NHÂN => NẾU TRÙNG THÌ THÔNG BÁO ĐÃ TỒN TÀI BỆNH NHÂN ĐÓ
   BẪY 3: MÃ BỆNH NHÂN KHÔNG TỒN TẠI => KHÔNG TÌM THẤY BỆNH NHÂN MÃ BN999 !
"""
LINE = "-"*83
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]
def find_patient_id_patient_list(patients_list, id_wanna_find):
    return next((i for i, value in enumerate(patients_list) if value.split("|")[0].strip() == id_wanna_find), -1)
def check_is_empty(patients_list):
    if not patients_list:
        return True
    return False
def check_is_a_number(numer):
    """
    HÀM ĐỂ CHECK NHẬN CÓ THỂ LÀ SOOS HAY KHÔNG !
    INPUT: BIẾN CẦN CHECK 
    OUTPUT: TRẢ VỀ BIẾN ĐÓ ĐƯỢC ÉP THÀNH INT HOẶC CÓ THỂ LÀ FALSE
    """
    try:
        if(check_is_empty_word(numer)):
            return False
        numer = int(numer)
        return numer
    except:
        return False
def check_is_empty_word(words):
    """ 
    HÀM ĐỂ CHECK XEM CÓ THẺ CHỮ CÓ ĐỂ TRỐNG KHÔNG !
    INPUT: CHỮ CẦN MUỐN CHECK
    OUTPUT: TRUE HOẶC LÀ FALSE NẾU SAI
    """
    if(words.isspace() or not words):
        return True
    return False 

def split_word_to_list(words):
    return words.strip().split("|")
def display_patient(patient_list):
    """ 
        HÀM ĐỂ HIỆN DANH SÁCH BỆNH NHÂN ĐIỀU TRỊ
        INPUT: DANH SÁCH BỆNH NHÂN
        OUTPUT: CÓ THỂ IN RA THEO BẢNG HOẶC IN LÀ KHOOGN CÓ BỆNH NHÂN NÀO
    """
    if(check_is_empty(patient_list)):
        print("Hệ thống hiện chưa có hồ sơ nào !")
    else:
        print(" BẢNG THEO DỠI CA CẤP CỨU ".center(83, "-"))
        print(f"{"MÃ":<10}  | {"TÊN":30} | {"NHỊP TIM":<20} | {"NHIỆT ĐỘ":<20}")
        print(LINE)
        for i, value in enumerate(patient_list):
            some = split_word_to_list(value)
            print(f"[{some[0] + "]":<10} | {some[1]:<30} | {some[2].split(":")[1] + " bmp":<20} | {some[3].split(":")[1] + " 'C":<20} ")
        print(LINE)
def insert_patient(patient_list):
    """ 
        HÀM THÊM BỆNH NHÂN MỚI VÀO DANH SÁCH
        INPUT: NHẬP DANH SÁCH VÀO BỆNH NHÂN
        OUTPUT: THÔNG BÁO THÊM THÀNH CÔNG
    """
    print(" TIẾP NHẬN BỆNH NHÂN MỚI ".center(83, "-"))
    while True: 
        patient_code = input("Vui lòng nhập mã ER: ").upper()
        if(check_is_empty_word(patient_code)):
            print("Mã bệnh nhân không được trống !")
            continue
        if(find_patient_id_patient_list(patient_list, patient_code) != -1):
            print("Mã bệnh nhân đã tồn tại tỏng hệ thống ! vui lòng kiểm tra lại !")
            continue 
        break 
    while True:
        patient_name = input("Vui lòng nhập tên bệnh nhân: ").title().replace("-", " ")
        if(check_is_empty_word(patient_name)):
            print("Tên bệnh nhân không được để trống !")
            continue 
        break 
    while True:
        patient_hear = input("Vui lòng nhập nhịp tim HR: ")
        if(not check_is_a_number(patient_hear)):
            print("Dữ liệu không phù hợp với nhịp tim")
            continue
        patient_hear = check_is_a_number(patient_hear) 
        if(patient_hear < 0):
            print("Nhịp tim không được âm")
            continue 
        break 
    while True:
        try:
            patient_tempo = float(input("Vui lòng nhập nhiệt độ TEMP: "))
        except ValueError:
            print("Nhiệt độ thân thể không đúng với dữ liệu")
            continue
        if(patient_tempo < 36.5):
            print("Sinh hiệu không hợp lệ !, vui lòng nhập số lớn hơn hoặc bằng 36.5 !")
            continue        
        break 
    patient_list.append(f"ER{patient_code.strip()}|{patient_name.strip()}|HR:{patient_hear}|TEMP:{patient_tempo}")
    print(
        "Thêm hồ sơ bệnh nhân thành công ! \n"
        "Sau khi chuẩn hóa, dữ liệu được lưu là: \n"
        f"ER{patient_code.strip()}|{patient_name.strip()}|HR:{patient_hear}|TEMP:{patient_tempo}"
        )
    print("Tiếp nhận ca cấp cứu mới thành công !")

def update_patient(patients_list):
    """ 
    HÀM ĐỂ CẬP NHẬT LẠI BỆNH CỦA BỆNH NHÂN VÀ CÓ FORMAT LẠI 
    INPUT: DANH SÁCH BỆNH NHÂN
    OUTPUT: THAY ĐỔI ĐƯỢC TÊN BỆNH MỚI
    """
    print(" CẬP NHẬT LẠI BỆNH NHÂN ".center(83, "-"))
    while True: 
        patient_code = input("Vui lòng nhập mã bệnh nhân: ").upper()
        if(check_is_empty_word(patient_code)):
            print("Mã bệnh nhân không được trống !")
            continue
        if(find_patient_id_patient_list(patients_list, patient_code) == -1):
            print("Mã bệnh nhân không tồn tại !")
            continue 
        break
    find_index = find_patient_id_patient_list(patients_list, patient_code)
    print(
        f"Tìm thấy bệnh nhân: {patients_list[find_index].split("|")[1]} \n"
        f"Sinh hiệu hiện tại: {patients_list[find_index].split("|")[2]} | {patients_list[find_index].split("|")[3]} \n"
    )
    while True:
        choose_to_update = input(
            "Bạn muốn cập nhật: \n"
            "1. Nhịp tim HR \n"
            "2. Nhiệt độ TEMP \n"
            ">> Chọn loại sinh hiệu: "
            ).strip()
        if(not choose_to_update):
            print("Lỗi lựa chọn không được để trống !")
            continue 
        if(choose_to_update not in ["1", "2"]):
            print("Lựa chọn nằm ngoài chức năng 1 và 2 !")
            continue 
        if(choose_to_update == "1"):
            while True:
                new_patient_hear = input("Vui lòng nhập nhịp tim HR: ")
                if(not check_is_a_number(new_patient_hear)):
                    print("Dữ liệu không phù hợp với nhịp tim")
                    continue
                new_patient_hear = check_is_a_number(new_patient_hear) 
                if(new_patient_hear < 0):
                    print("Nhịp tim không được âm")
                    continue 
                break
        else:
            while True:
                try:
                    new_patient_tempo = float(input("Vui lòng nhập nhiệt độ TEMP: "))
                except ValueError:
                    print("Nhiệt độ thân thể không đúng với dữ liệu")
                    continue
                if(new_patient_tempo < 36.5):
                    print("Sinh hiệu không hợp lệ !, vui lòng nhập số lớn hơn hoặc bằng 36.5 !")
                    continue        
                break 
        break 
    current_patient = patients_list[find_index].split("|")

    if choose_to_update == "1":
        result = "|".join([current_patient[0], current_patient[1], f"HR:{new_patient_hear}", current_patient[3]])
    else:
        result = "|".join([current_patient[0], current_patient[1], current_patient[2], f"TEMP:{new_patient_tempo}"])
    patients_list[find_index] = result
    print("Đã cập nhật bệnh thành công !") 
    print(f"Dữ liệu mới được lưu: \n{result}")

def check_red_alert(patients):
    red_list = []
    for item in patients:
        current_part = split_word_to_list(item)
        if(int(current_part[2].split(":")[1]) > 100 or float(current_part[3].split(":")[1]) >=39.0):
            red_list.append(item)
    return red_list
        
def trigger_red_alert(patients):
    if(check_is_empty(patients)):
        print("Khoa cấp cứu hiện đang trống..")
    else:
        list_to = check_red_alert(patients)
        print("!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")
        print(f"{"MÃ":<10}  | {"TÊN":30} | {"NHỊP TIM":<20} | {"NHIỆT ĐỘ":<20}")
        print(LINE*2)
        for i, value in enumerate(list_to):
            some = split_word_to_list(value)
            print(f"[{some[0] + "]":<10} | {some[1]:<30} | {some[2].split(":")[1] + " bmp":<20} | {some[3].split(":")[1] + " 'C":<20} | CẦN ĐƯỢC XỬ LÝ KHẨN CẤP")
        print(LINE*2)
        print(f"Tổng số ca nguy kịch {len(list_to)}")
def discharge_patient(patients):
    print(" TIẾP NHẬN BỆNH NHÂN MỚI ".center(83, "-"))
    while True: 
        patient_code = input("Vui lòng nhập mã bệnh nhân: ").upper()
        if(check_is_empty_word(patient_code)):
            print("Mã bệnh nhân không được trống !")
            continue
        if(find_patient_id_patient_list(patients, patient_code) == -1):
            print("Mã bệnh nhân không tồn tại !")
            continue 
        break
    find_index = find_patient_id_patient_list(patients, patient_code)
    print(
        f"Tìm thấy bệnh nhân: {patients[find_index].split("|")[1]} \n"
        f"Sinh hiệu hiện tại: {patients[find_index].split("|")[2]} | {patients[find_index].split("|")[3]} \n"
    )
    while True:
        yes_or_no = input("Bạn có muốn xóa bệnh nhân này (Y - N): ").strip().upper()
        if(not yes_or_no):
            print("Không được để trống !")
            continue 
        if(yes_or_no not in ["Y", "N"]):
            print("Bạn chỉ được nhập Y cho Yes, N cho No !")
            continue 
        break 
    if(yes_or_no == "Y"):
        patient_name = patients[find_index].split("|")[1]
        patients.pop(find_index)
        print(f"Đã chuyển khoa cho bệnh nhân {patient_name}")
    else:
        print("Đã hủy hoàn tác xóa !")
def show_menu():
    """ 
    HÀM HIỆN MENU CHO NGƯỜI DÙNG
    INPUT: KHÔNG CÓ
    OUTPUT: HIỆN MENU CHO NGƯỜI DÙNG ĐỂ NHẬP
    """
    return (input(
        f"==== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER ====\n"
        f"[1]. Bảng theo dõi bệnh nhân \n"
        f"[2]. Tiếp nhận ca cấp cứu mới \n"
        f"[3]. Cập nhật lại sinh hiệu \n"
        f"[4]. BÁO ĐỘNG ĐỎ lọc bệnh nhân nguy kịch \n"
        f"[5]. Xuất viện / Chuyển khoa \n"
        f"[6]. Thoát chương trình \n"
        f"===========================================\n"
        f">>> Nhập lựa chọn của bạn: "
        ))
def main():
    """ 
    HÀM THỰC HIỆN CHÍNH THỨC
    INPUT: KHÔNG
    OUTPUT: KHÔNG 
    """
    while True:
        choose = check_is_a_number(show_menu())
        if(not choose):
            print()
            print("Lựa chọn không phù hợp")
            print()
            continue 
        match choose:
            case 1:
                print()
                display_patient(patient_list=er_patients)
                print()
            case 2:
                print()
                insert_patient(patient_list=er_patients)
                print()
            case 3:
                print()
                update_patient(patients_list=er_patients)
                print()
            case 4:
                print()
                trigger_red_alert(patients=er_patients)
                print()
            case 5:
                print()
                discharge_patient(patients=er_patients)
                print()
            case 6:
                print()
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                print()
                break 
            case _:
                print("Lựa chọn không phù hợp !")    
            
if __name__ == "__main__":
    main()
