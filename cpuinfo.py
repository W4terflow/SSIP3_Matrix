import multiprocessing
import platform

def main():
    # Получаем информацию о процессоре
    processor_info = platform.processor() or "Информация не доступна"
    # Получаем количество ядер
    cores = multiprocessing.cpu_count()
    
    print("Информация о процессоре:")
    print(f"Модель: {processor_info}")
    print(f"Количество ядер: {cores}")

if __name__ == "__main__":
    main()
