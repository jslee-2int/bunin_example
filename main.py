import sys, os
from ui_main import Ui_MainWindow

import pandas as pd
import numpy as np
import threading

from PyQt5 import QtCore, QtWidgets, QtGui
import configparser

from datetime import datetime
from dateutil.relativedelta import relativedelta

from serial_comm import Serial_comm


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    send_instance_singal = QtCore.pyqtSignal("PyQt_PyObject")

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btn_home.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        self.Debug_val = True

        # draggable window
        self.center()
        self.oldPos = self.pos()

        # Configuration
        self.onlyInt = QtGui.QIntValidator()
        self.lineEdit_st.setValidator(self.onlyInt)
        self.lineEdit_st_7.setValidator(self.onlyInt)

        self.config = configparser.ConfigParser()
        self.config.read('setting.ini', "utf8")
        self.lineEdit_st.setText(self.config['Setting']['durating_time'])
        self.lineEdit_st_2.setText(self.config['Setting']['file_name'])
        self.lineEdit_st_3.setText(self.config['Setting']['operator'])
        self.lineEdit_st_4.setText(self.config['Setting']['template_file_open'])
        self.lineEdit_st_5.setText(self.config['Setting']['save_folder_path'])
        self.lineEdit_st_7.setText(self.config['Setting']['time_interval'])

        self.serial_connect_list = self.config['instrument']['arduino_port_list'].split(',')

        self.pushButton_st.clicked.connect(self.file_dialog_tfo)
        self.pushButton_st_2.clicked.connect(self.file_dialog_sf)
        self.pushButton_st_3.clicked.connect(self.save_setting)
        self.pushButton_st_4.clicked.connect(self.restore_setting)

        # Configuration plot :: init. values
        self.mpd_plot = 'ch1'
        self.ther_plot = 'ch1'
        self.tec_volt_plot = 'ch1'
        self.tec_curr_plot = 'ch1'
        self.ld_volt_plot = 'ch1'
        self.ld_curr_plot = 'ch1'

        # Menu Btn.
        self.btn_home.clicked.connect(self.btn_menu_1)
        self.btn_mpd.clicked.connect(self.btn_menu_2)
        self.btn_ther.clicked.connect(self.btn_menu_3)
        self.btn_tec_volt.clicked.connect(self.btn_menu_4)
        self.btn_tec_curr.clicked.connect(self.btn_menu_5)
        self.btn_ld_volt.clicked.connect(self.btn_menu_6)
        self.btn_ld_curr.clicked.connect(self.btn_menu_7)
        self.btn_setting.clicked.connect(self.btn_menu_8)

        # MPD Ch. Btn connect
        self.bnt_mpd.clicked.connect(lambda: self.btn_plot_test('mpd_ch1'))
        self.bnt_mpd_2.clicked.connect(lambda: self.btn_plot_test('mpd_ch2'))
        self.bnt_mpd_3.clicked.connect(lambda: self.btn_plot_test('mpd_ch3'))
        self.bnt_mpd_4.clicked.connect(lambda: self.btn_plot_test('mpd_ch4'))
        self.bnt_mpd_5.clicked.connect(lambda: self.btn_plot_test('mpd_ch5'))
        self.bnt_mpd_6.clicked.connect(lambda: self.btn_plot_test('mpd_ch6'))
        self.bnt_mpd_7.clicked.connect(lambda: self.btn_plot_test('mpd_ch7'))
        self.bnt_mpd_8.clicked.connect(lambda: self.btn_plot_test('mpd_ch8'))
        self.bnt_mpd_9.clicked.connect(lambda: self.btn_plot_test('mpd_ch9'))
        self.bnt_mpd_10.clicked.connect(lambda: self.btn_plot_test('mpd_ch10'))
        self.bnt_mpd_11.clicked.connect(lambda: self.btn_plot_test('mpd_ch11'))
        self.bnt_mpd_12.clicked.connect(lambda: self.btn_plot_test('mpd_ch12'))
        self.bnt_mpd_13.clicked.connect(lambda: self.btn_plot_test('mpd_ch13'))
        self.bnt_mpd_14.clicked.connect(lambda: self.btn_plot_test('mpd_ch14'))
        self.bnt_mpd_15.clicked.connect(lambda: self.btn_plot_test('mpd_ch15'))
        self.bnt_mpd_16.clicked.connect(lambda: self.btn_plot_test('mpd_ch16'))

        # Thermistor Ch. Btn connect
        self.bnt_them.clicked.connect(lambda: self.btn_plot_test('them_ch1'))
        self.bnt_them_2.clicked.connect(lambda: self.btn_plot_test('them_ch2'))
        self.bnt_them_3.clicked.connect(lambda: self.btn_plot_test('them_ch3'))
        self.bnt_them_4.clicked.connect(lambda: self.btn_plot_test('them_ch4'))
        self.bnt_them_5.clicked.connect(lambda: self.btn_plot_test('them_ch5'))
        self.bnt_them_6.clicked.connect(lambda: self.btn_plot_test('them_ch6'))
        self.bnt_them_7.clicked.connect(lambda: self.btn_plot_test('them_ch7'))
        self.bnt_them_8.clicked.connect(lambda: self.btn_plot_test('them_ch8'))
        self.bnt_them_9.clicked.connect(lambda: self.btn_plot_test('them_ch9'))
        self.bnt_them_10.clicked.connect(lambda: self.btn_plot_test('them_ch10'))
        self.bnt_them_11.clicked.connect(lambda: self.btn_plot_test('them_ch11'))
        self.bnt_them_12.clicked.connect(lambda: self.btn_plot_test('them_ch12'))
        self.bnt_them_13.clicked.connect(lambda: self.btn_plot_test('them_ch13'))
        self.bnt_them_14.clicked.connect(lambda: self.btn_plot_test('them_ch14'))
        self.bnt_them_15.clicked.connect(lambda: self.btn_plot_test('them_ch15'))
        self.bnt_them_16.clicked.connect(lambda: self.btn_plot_test('them_ch16'))

        # TEC Voltage Ch. Btn Connect
        self.bnt_tv.clicked.connect(lambda: self.btn_plot_test('tv_ch1'))
        self.bnt_tv_2.clicked.connect(lambda: self.btn_plot_test('tv_ch2'))
        self.bnt_tv_3.clicked.connect(lambda: self.btn_plot_test('tv_ch3'))
        self.bnt_tv_4.clicked.connect(lambda: self.btn_plot_test('tv_ch4'))
        self.bnt_tv_5.clicked.connect(lambda: self.btn_plot_test('tv_ch5'))
        self.bnt_tv_6.clicked.connect(lambda: self.btn_plot_test('tv_ch6'))
        self.bnt_tv_7.clicked.connect(lambda: self.btn_plot_test('tv_ch7'))
        self.bnt_tv_8.clicked.connect(lambda: self.btn_plot_test('tv_ch8'))
        self.bnt_tv_9.clicked.connect(lambda: self.btn_plot_test('tv_ch9'))
        self.bnt_tv_10.clicked.connect(lambda: self.btn_plot_test('tv_ch10'))
        self.bnt_tv_11.clicked.connect(lambda: self.btn_plot_test('tv_ch11'))
        self.bnt_tv_12.clicked.connect(lambda: self.btn_plot_test('tv_ch12'))
        self.bnt_tv_13.clicked.connect(lambda: self.btn_plot_test('tv_ch13'))
        self.bnt_tv_14.clicked.connect(lambda: self.btn_plot_test('tv_ch14'))
        self.bnt_tv_15.clicked.connect(lambda: self.btn_plot_test('tv_ch15'))
        self.bnt_tv_16.clicked.connect(lambda: self.btn_plot_test('tv_ch16'))

        # TEC Current Ch. Btn. connect
        self.bnt_tc.clicked.connect(lambda: self.btn_plot_test('tc_ch1'))
        self.bnt_tc_2.clicked.connect(lambda: self.btn_plot_test('tc_ch2'))
        self.bnt_tc_3.clicked.connect(lambda: self.btn_plot_test('tc_ch3'))
        self.bnt_tc_4.clicked.connect(lambda: self.btn_plot_test('tc_ch4'))
        self.bnt_tc_5.clicked.connect(lambda: self.btn_plot_test('tc_ch5'))
        self.bnt_tc_6.clicked.connect(lambda: self.btn_plot_test('tc_ch6'))
        self.bnt_tc_7.clicked.connect(lambda: self.btn_plot_test('tc_ch7'))
        self.bnt_tc_8.clicked.connect(lambda: self.btn_plot_test('tc_ch8'))
        self.bnt_tc_9.clicked.connect(lambda: self.btn_plot_test('tc_ch9'))
        self.bnt_tc_10.clicked.connect(lambda: self.btn_plot_test('tc_ch10'))
        self.bnt_tc_11.clicked.connect(lambda: self.btn_plot_test('tc_ch11'))
        self.bnt_tc_12.clicked.connect(lambda: self.btn_plot_test('tc_ch12'))
        self.bnt_tc_13.clicked.connect(lambda: self.btn_plot_test('tc_ch13'))
        self.bnt_tc_14.clicked.connect(lambda: self.btn_plot_test('tc_ch14'))
        self.bnt_tc_15.clicked.connect(lambda: self.btn_plot_test('tc_ch15'))
        self.bnt_tc_16.clicked.connect(lambda: self.btn_plot_test('tc_ch16'))

        # LD Voltage Ch. Btn. Connect
        self.bnt_ldv.clicked.connect(lambda: self.btn_plot_test('ldv_ch1'))
        self.bnt_ldv_2.clicked.connect(lambda: self.btn_plot_test('ldv_ch2'))
        self.bnt_ldv_3.clicked.connect(lambda: self.btn_plot_test('ldv_ch3'))
        self.bnt_ldv_4.clicked.connect(lambda: self.btn_plot_test('ldv_ch4'))
        self.bnt_ldv_5.clicked.connect(lambda: self.btn_plot_test('ldv_ch5'))
        self.bnt_ldv_6.clicked.connect(lambda: self.btn_plot_test('ldv_ch6'))
        self.bnt_ldv_7.clicked.connect(lambda: self.btn_plot_test('ldv_ch7'))
        self.bnt_ldv_8.clicked.connect(lambda: self.btn_plot_test('ldv_ch8'))
        self.bnt_ldv_9.clicked.connect(lambda: self.btn_plot_test('ldv_ch9'))
        self.bnt_ldv_10.clicked.connect(lambda: self.btn_plot_test('ldv_ch10'))
        self.bnt_ldv_11.clicked.connect(lambda: self.btn_plot_test('ldv_ch11'))
        self.bnt_ldv_12.clicked.connect(lambda: self.btn_plot_test('ldv_ch12'))
        self.bnt_ldv_13.clicked.connect(lambda: self.btn_plot_test('ldv_ch13'))
        self.bnt_ldv_14.clicked.connect(lambda: self.btn_plot_test('ldv_ch14'))
        self.bnt_ldv_15.clicked.connect(lambda: self.btn_plot_test('ldv_ch15'))
        self.bnt_ldv_16.clicked.connect(lambda: self.btn_plot_test('ldv_ch16'))

        # LD Currnet Ch. Btn. Connect
        self.bnt_ldc.clicked.connect(lambda: self.btn_plot_test('ldc_ch1'))
        self.bnt_ldc_2.clicked.connect(lambda: self.btn_plot_test('ldc_ch2'))
        self.bnt_ldc_3.clicked.connect(lambda: self.btn_plot_test('ldc_ch3'))
        self.bnt_ldc_4.clicked.connect(lambda: self.btn_plot_test('ldc_ch4'))
        self.bnt_ldc_5.clicked.connect(lambda: self.btn_plot_test('ldc_ch5'))
        self.bnt_ldc_6.clicked.connect(lambda: self.btn_plot_test('ldc_ch6'))
        self.bnt_ldc_7.clicked.connect(lambda: self.btn_plot_test('ldc_ch7'))
        self.bnt_ldc_8.clicked.connect(lambda: self.btn_plot_test('ldc_ch8'))
        self.bnt_ldc_9.clicked.connect(lambda: self.btn_plot_test('ldc_ch9'))
        self.bnt_ldc_10.clicked.connect(lambda: self.btn_plot_test('ldc_ch10'))
        self.bnt_ldc_11.clicked.connect(lambda: self.btn_plot_test('ldc_ch11'))
        self.bnt_ldc_12.clicked.connect(lambda: self.btn_plot_test('ldc_ch12'))
        self.bnt_ldc_13.clicked.connect(lambda: self.btn_plot_test('ldc_ch13'))
        self.bnt_ldc_14.clicked.connect(lambda: self.btn_plot_test('ldc_ch14'))
        self.bnt_ldc_15.clicked.connect(lambda: self.btn_plot_test('ldc_ch15'))
        self.bnt_ldc_16.clicked.connect(lambda: self.btn_plot_test('ldc_ch16'))

        # Multi Threading define
        # self.pushButton_start.clicked.connect(self.time_start)
        # self.pushButton_stop.clicked.connect(self.time_stop)
        self.pushButton_start.clicked.connect(lambda: self.time_start(self.serial_connect_list[0], 38400))
        self.pushButton_start_2.clicked.connect(lambda: self.time_start_2(self.serial_connect_list[1], 38400))
        self.pushButton_start_3.clicked.connect(lambda: self.time_start_3(self.serial_connect_list[2], 38400))
        self.pushButton_start_4.clicked.connect(lambda: self.time_start_4(self.serial_connect_list[3], 38400))
        self.pushButton_start_5.clicked.connect(lambda: self.time_start_5(self.serial_connect_list[4], 38400))
        self.pushButton_start_6.clicked.connect(lambda: self.time_start_6(self.serial_connect_list[5], 38400))
        self.pushButton_start_7.clicked.connect(lambda: self.time_start_7(self.serial_connect_list[6], 38400))
        self.pushButton_start_8.clicked.connect(lambda: self.time_start_8(self.serial_connect_list[7], 38400))
        self.pushButton_start_9.clicked.connect(lambda: self.time_start_9(self.serial_connect_list[8], 38400))
        self.pushButton_start_10.clicked.connect(lambda: self.time_start_10(self.serial_connect_list[9], 38400))
        self.pushButton_start_11.clicked.connect(lambda: self.time_start_11(self.serial_connect_list[10], 38400))
        self.pushButton_start_12.clicked.connect(lambda: self.time_start_12(self.serial_connect_list[11], 38400))
        self.pushButton_start_13.clicked.connect(lambda: self.time_start_13(self.serial_connect_list[12], 38400))
        self.pushButton_start_14.clicked.connect(lambda: self.time_start_14(self.serial_connect_list[13], 38400))
        self.pushButton_start_15.clicked.connect(lambda: self.time_start_15(self.serial_connect_list[14], 38400))
        self.pushButton_start_16.clicked.connect(lambda: self.time_start_16(self.serial_connect_list[15], 38400))
        self.pushButton_stop.clicked.connect(self.time_stop)
        self.pushButton_stop_2.clicked.connect(self.time_stop_2)
        self.pushButton_stop_3.clicked.connect(self.time_stop_3)
        self.pushButton_stop_4.clicked.connect(self.time_stop_4)
        self.pushButton_stop_5.clicked.connect(self.time_stop_5)
        self.pushButton_stop_6.clicked.connect(self.time_stop_6)
        self.pushButton_stop_7.clicked.connect(self.time_stop_7)
        self.pushButton_stop_8.clicked.connect(self.time_stop_8)
        self.pushButton_stop_9.clicked.connect(self.time_stop_9)
        self.pushButton_stop_10.clicked.connect(self.time_stop_10)
        self.pushButton_stop_11.clicked.connect(self.time_stop_11)
        self.pushButton_stop_12.clicked.connect(self.time_stop_12)
        self.pushButton_stop_13.clicked.connect(self.time_stop_13)
        self.pushButton_stop_14.clicked.connect(self.time_stop_14)
        self.pushButton_stop_15.clicked.connect(self.time_stop_15)
        self.pushButton_stop_16.clicked.connect(self.time_stop_16)

        self.init_state_btn()

        # Data list & dict & frame
        # Ch1 col : [ Data , MPD, Thermistor, TEC_Voltage, TEC_Current, LD_Voltage, LD_Current ]

        self.df_ch1, self.df_ch2, self.df_ch3, self.df_ch4, self.df_ch5, self.df_ch6, self.df_ch7, self.df_ch8, \
        self.df_ch9, self.df_ch10, self.df_ch11, self.df_ch12, self.df_ch13, self.df_ch14, self.df_ch15, self.df_ch16 \
            = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        self.df_bundle = [self.df_ch1, self.df_ch2, self.df_ch3, self.df_ch4, self.df_ch5, self.df_ch6, self.df_ch7,
                          self.df_ch8, self.df_ch9, self.df_ch10, self.df_ch11, self.df_ch12, self.df_ch13, self.df_ch14,
                          self.df_ch15, self.df_ch16]

        for i in range(16):
            for j in range(16):
                self.df_bundle[i].append(pd.DataFrame({'Date': [], 'MPD': [], 'Thermistor': [], 'TEC_Voltage': [],
                                                          'TEC_Current': [], 'LD_Voltage': [], 'LD_Current': []}))

    def btn_plot_test(self, name):
        if 'mpd_' in name:
            self.mpd_plot = name.replace('mpd_', '')
            index_no = int(name.replace('mpd_ch', '')) - 1
            date_list, x_data = [], []
            for j in range(16):
                date_list.append(np.array(self.df_bundle[index_no][j]['Date']).tolist())
                x_data.append(np.array(self.df_bundle[index_no][j]['MPD']).tolist())
            self.plot_mpd(title='MPD Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)
        if 'them_' in name:
            self.ther_plot = name.replace('them_', '')
            index_no = int(name.replace('them_ch', '')) - 1
            for i in range(16):
                if index_no == i:
                    date_list, x_data = [], []
                    for j in range(16):
                        date_list.append(np.array(self.df_bundle[i][j]['Date']).tolist())
                        x_data.append(np.array(self.df_bundle[i][j]['Thermistor']).tolist())
                    self.plot_thrm(title='Thermistor Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)
        if 'tv_' in name:
            self.tec_volt_plot = name.replace('tv_', '')
            index_no = int(name.replace('tv_ch', '')) - 1
            for i in range(16):
                if index_no == i:
                    date_list, x_data = [], []
                    for j in range(16):
                        date_list.append(np.array(self.df_bundle[i][j]['Date']).tolist())
                        x_data.append(np.array(self.df_bundle[i][j]['TEC_Voltage']).tolist())
                    self.plot_tec_volt(title='TEC Voltage Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)
        if 'tc_' in name:
            self.tec_curr_plot = name.replace('tc_', '')
            index_no = int(name.replace('tc_ch', '')) - 1
            for i in range(16):
                if index_no == i:
                    date_list, x_data = [], []
                    for j in range(16):
                        date_list.append(np.array(self.df_bundle[i][j]['Date']).tolist())
                        x_data.append(np.array(self.df_bundle[i][j]['TEC_Current']).tolist())
                    self.plot_tec_curr(title='TEC Current Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)
        if 'ldv_' in name:
            self.ld_volt_plot = name.replace('ldv_', '')
            index_no = int(name.replace('ldv_ch', '')) - 1
            for i in range(16):
                if index_no == i:
                    date_list, x_data = [], []
                    for j in range(16):
                        date_list.append(np.array(self.df_bundle[i][j]['Date']).tolist())
                        x_data.append(np.array(self.df_bundle[i][j]['LD_Voltage']).tolist())
                    self.plot_ld_volt(title='LD Voltage Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)
        if 'ldc_' in name:
            self.ld_curr_plot = name.replace('ldc_', '')
            index_no = int(name.replace('ldc_ch', '')) - 1
            for i in range(16):
                if index_no == i:
                    date_list, x_data = [], []
                    for j in range(16):
                        date_list.append(np.array(self.df_bundle[i][j]['Date']).tolist())
                        x_data.append(np.array(self.df_bundle[i][j]['LD_Current']).tolist())
                    self.plot_ld_curr(title='LD Current Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=x_data)

    def plot_update(self):
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.mpd_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            mpd_list.append(np.array(self.df_bundle[index_no][i]['MPD']).tolist())
        self.plot_mpd(title='MPD Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=mpd_list)
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.ther_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            ther_list.append(np.array(self.df_bundle[index_no][i]['Thermistor']).tolist())
        self.plot_thrm(title='Thermistor Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=ther_list)
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.tec_volt_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            ther_list.append(np.array(self.df_bundle[index_no][i]['TEC_Voltage']).tolist())
        self.plot_tec_volt(title='TEC Voltage Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=ther_list)
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.tec_curr_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            ther_list.append(np.array(self.df_bundle[index_no][i]['TEC_Current']).tolist())
        self.plot_tec_curr(title='TEC Current Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=ther_list)
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.ld_volt_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            ther_list.append(np.array(self.df_bundle[index_no][i]['LD_Voltage']).tolist())
        self.plot_ld_volt(title='LD Voltage Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=ther_list)
        date_list, mpd_list, ther_list, tec_volt_list, tec_curr_list, ld_volt_list, ld_curr_list = [], [], [], [], [], [], []
        index_no = int(self.ld_curr_plot.replace('ch', '')) - 1
        for i in range(16):
            date_list.append(np.array(self.df_bundle[index_no][i]['Date']).tolist())
            ther_list.append(np.array(self.df_bundle[index_no][i]['LD_Current']).tolist())
        self.plot_ld_curr(title='LD Current Chart :: Ch {}'.format(index_no+1), x_data=date_list, y_data=ther_list)

    def df_update(self, duration_time_sec, index_no, list_msg):
        date_val = duration_time_sec
        mpd_val = list_msg[index_no][0]
        ther_val = list_msg[index_no][1]
        tec_volt_val = list_msg[index_no][2]
        tec_curr_val = list_msg[index_no][3]
        ld_volta_val = list_msg[index_no][4]
        ld_curr_val = list_msg[index_no][5]

        df = pd.DataFrame(
            {'Date': [date_val], 'MPD': [mpd_val], 'Thermistor': [ther_val], 'TEC_Voltage': [tec_volt_val],
             'TEC_Current': [tec_curr_val], 'LD_Voltage': [ld_volta_val], 'LD_Current': [ld_curr_val]})
        return df

    def hex_to_dec(self, hex_df):
        msg_dex = []
        for i in range(16):
            list_b = []
            for j in range(6):
                list_b.append(int(hex_df[i][j], 16))
            msg_dex.append(list_b)
        return msg_dex

    # Multi Threading
    @QtCore.pyqtSlot()
    def time_start(self, port, baud):
        try:
            self.port_ch = Serial_comm(port=port, baud=baud)

            self.th = Worker(self.port_ch, parent=self)
            self.th.sec_changed.connect(self.time_update)

            self.pushButton_start.setEnabled(False)
            self.pushButton_stop.setEnabled(True)
            # Cal. Time & delta
            self.start_time = datetime.now()
            self.end_time = self.start_time + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_str = self.start_time.isoformat(timespec='seconds')
            self.end_time_str = self.end_time.isoformat(timespec='seconds')
            self.start_time_str, self.end_time_str = self.start_time_str.replace("T", ' '), self.end_time_str.replace("T",
                                                                                                                      ' ')
            self.label_c1_2.setText(self.start_time_str)
            self.label_c1_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c1_3.setText(self.end_time_str)
            self.label_c1_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c1_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th.start()
            self.th.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_2(self, port, baud):
        try:
            self.port_ch2 = Serial_comm(port=port, baud=baud)

            self.th_2 = Worker(self.port_ch2, parent=self)
            self.th_2.sec_changed.connect(self.time_update_2)

            self.pushButton_start_2.setEnabled(False)
            self.pushButton_stop_2.setEnabled(True)
            # Cal. Time & delta
            self.start_time_2 = datetime.now()
            self.end_time_2 = self.start_time_2 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_2_str = self.start_time_2.isoformat(timespec='seconds')
            self.end_time_2_str = self.end_time_2.isoformat(timespec='seconds')
            self.start_time_2_str, self.end_time_2_str = self.start_time_2_str.replace("T", ' '), self.end_time_2_str.replace("T",' ')

            self.label_c2_2.setText(self.start_time_2_str)
            self.label_c2_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c2_3.setText(self.end_time_2_str)
            self.label_c2_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c2_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_2.start()
            self.th_2.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_3(self, port, baud):
        try:
            self.port_ch3 = Serial_comm(port=port, baud=baud)
            self.th_3 = Worker(self.port_ch3, parent=self)
            self.th_3.sec_changed.connect(self.time_update_3)

            # Cal. Time & delta
            self.start_time_3 = datetime.now()
            self.end_time_3 = self.start_time_3 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_3_str = self.start_time_3.isoformat(timespec='seconds')
            self.end_time_3_str = self.end_time_3.isoformat(timespec='seconds')
            self.start_time_3_str = self.start_time_3_str.replace("T", ' ')
            self.end_time_3_str = self.end_time_3_str.replace("T", ' ')

            self.label_c3_2.setText(self.start_time_3_str)
            self.label_c3_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c3_3.setText(self.end_time_3_str)
            self.label_c3_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c3_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_3.start()
            self.th_3.working = True

            self.pushButton_start_3.setEnabled(False)
            self.pushButton_stop_3.setEnabled(True)
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_4(self, port, baud):
        try:
            self.port_ch4 = Serial_comm(port=port, baud=baud)
            self.th_4 = Worker(self.port_ch4, parent=self)
            self.th_4.sec_changed.connect(self.time_update_4)

            self.pushButton_start_4.setEnabled(False)
            self.pushButton_stop_4.setEnabled(True)
            # Cal. Time & delta
            self.start_time_4 = datetime.now()
            self.end_time_4 = self.start_time_4 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_4_str = self.start_time_4.isoformat(timespec='seconds')
            self.end_time_4_str = self.end_time_4.isoformat(timespec='seconds')
            self.start_time_4_str = self.start_time_4_str.replace("T", ' ')
            self.end_time_4_str = self.end_time_4_str.replace("T", ' ')
            self.label_c4_2.setText(self.start_time_4_str)
            self.label_c4_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c4_3.setText(self.end_time_4_str)
            self.label_c4_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c4_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_4.start()
            self.th_4.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_5(self, port, baud):
        try:
            self.port_ch5 = Serial_comm(port=port, baud=baud)
            self.th_5 = Worker(self.port_ch5, parent=self)
            self.th_5.sec_changed.connect(self.time_update_5)

            self.pushButton_start_5.setEnabled(False)
            self.pushButton_stop_5.setEnabled(True)
            # Cal. Time & delta
            self.start_time_5 = datetime.now()
            self.end_time_5 = self.start_time_5 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_5_str = self.start_time_5.isoformat(timespec='seconds')
            self.end_time_5_str = self.end_time_5.isoformat(timespec='seconds')
            self.start_time_5_str = self.start_time_5_str.replace("T", ' ')
            self.end_time_5_str = self.end_time_5_str.replace("T", ' ')
            self.label_c5_2.setText(self.start_time_5_str)
            self.label_c5_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c5_3.setText(self.end_time_5_str)
            self.label_c5_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c5_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_5.start()
            self.th_5.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_6(self, port, baud):
        try:
            self.port_ch6 = Serial_comm(port=port, baud=baud)
            self.th_6 = Worker(self.port_ch7, parent=self)
            self.th_6.sec_changed.connect(self.time_update_6)

            self.pushButton_start_6.setEnabled(False)
            self.pushButton_stop_6.setEnabled(True)
            # Cal. Time & delta
            self.start_time_6 = datetime.now()
            self.end_time_6 = self.start_time_6 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_6_str = self.start_time_6.isoformat(timespec='seconds')
            self.end_time_6_str = self.end_time_6.isoformat(timespec='seconds')
            self.start_time_6_str = self.start_time_6_str.replace("T", ' ')
            self.end_time_6_str = self.end_time_6_str.replace("T", ' ')
            self.label_c6_2.setText(self.start_time_6_str)
            self.label_c6_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c6_3.setText(self.end_time_6_str)
            self.label_c6_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c6_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_6.start()
            self.th_6.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_7(self, port, baud):
        try:
            self.port_ch7 = Serial_comm(port=port, baud=baud)
            self.th_7 = Worker(self.port_ch7, parent=self)
            self.th_7.sec_changed.connect(self.time_update_7)

            self.pushButton_start_7.setEnabled(False)
            self.pushButton_stop_7.setEnabled(True)
            # Cal. Time & delta
            self.start_time_7 = datetime.now()
            self.end_time_7 = self.start_time_7 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_7_str = self.start_time_7.isoformat(timespec='seconds')
            self.end_time_7_str = self.end_time_7.isoformat(timespec='seconds')
            self.start_time_7_str = self.start_time_7_str.replace("T", ' ')
            self.end_time_7_str = self.end_time_7_str.replace("T", ' ')
            self.label_c7_2.setText(self.start_time_7_str)
            self.label_c7_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c7_3.setText(self.end_time_7_str)
            self.label_c7_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c7_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_7.start()
            self.th_7.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_8(self, port, baud):
        try:
            self.port_ch8 = Serial_comm(port=port, baud=baud)
            self.th_8 = Worker(self.port_ch8, parent=self)
            self.th_8.sec_changed.connect(self.time_update_8)

            self.pushButton_start_8.setEnabled(False)
            self.pushButton_stop_8.setEnabled(True)
            # Cal. Time & delta
            self.start_time_8 = datetime.now()
            self.end_time_8 = self.start_time_8 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_8_str = self.start_time_8.isoformat(timespec='seconds')
            self.end_time_8_str = self.end_time_8.isoformat(timespec='seconds')
            self.start_time_8_str = self.start_time_8_str.replace("T", ' ')
            self.end_time_8_str = self.end_time_8_str.replace("T", ' ')
            self.label_c8_2.setText(self.start_time_8_str)
            self.label_c8_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c8_3.setText(self.end_time_8_str)
            self.label_c8_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c8_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_8.start()
            self.th_8.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_9(self, port, baud):
        try:
            self.port_ch9 = Serial_comm(port=port, baud=baud)
            self.th_9 = Worker(self.port_ch9, parent=self)
            self.th_9.sec_changed.connect(self.time_update_9)

            self.pushButton_start_9.setEnabled(False)
            self.pushButton_stop_9.setEnabled(True)
            # Cal. Time & delta
            self.start_time_9 = datetime.now()
            self.end_time_9 = self.start_time_9 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_9_str = self.start_time_9.isoformat(timespec='seconds')
            self.end_time_9_str = self.end_time_9.isoformat(timespec='seconds')
            self.start_time_9_str = self.start_time_9_str.replace("T", ' ')
            self.end_time_9_str = self.end_time_9_str.replace("T", ' ')
            self.label_c9_2.setText(self.start_time_9_str)
            self.label_c9_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c9_3.setText(self.end_time_9_str)
            self.label_c9_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c9_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_9.start()
            self.th_9.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_10(self, port, baud):
        try:
            self.port_ch10 = Serial_comm(port=port, baud=baud)
            self.th_10 = Worker(self.port_ch10, parent=self)
            self.th_10.sec_changed.connect(self.time_update_10)

            self.pushButton_start_10.setEnabled(False)
            self.pushButton_stop_10.setEnabled(True)
            # Cal. Time & delta
            self.start_time_10 = datetime.now()
            self.end_time_10 = self.start_time_10 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_10_str = self.start_time_10.isoformat(timespec='seconds')
            self.end_time_10_str = self.end_time_10.isoformat(timespec='seconds')
            self.start_time_10_str = self.start_time_10_str.replace("T", ' ')
            self.end_time_10_str = self.end_time_10_str.replace("T", ' ')
            self.label_c10_2.setText(self.start_time_10_str)
            self.label_c10_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c10_3.setText(self.end_time_10_str)
            self.label_c10_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c10_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_10.start()
            self.th_10.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_11(self, port, baud):
        try:
            self.port_ch11 = Serial_comm(port=port, baud=baud)
            self.th_11 = Worker(self.port_ch11, parent=self)
            self.th_11.sec_changed.connect(self.time_update_11)

            self.pushButton_start_11.setEnabled(False)
            self.pushButton_stop_11.setEnabled(True)
            # Cal. Time & delta
            self.start_time_11 = datetime.now()
            self.end_time_11 = self.start_time_11 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_11_str = self.start_time_11.isoformat(timespec='seconds')
            self.end_time_11_str = self.end_time_11.isoformat(timespec='seconds')
            self.start_time_11_str = self.start_time_11_str.replace("T", ' ')
            self.end_time_11_str = self.end_time_11_str.replace("T", ' ')
            self.label_c11_2.setText(self.start_time_11_str)
            self.label_c11_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c11_3.setText(self.end_time_11_str)
            self.label_c11_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c11_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_11.start()
            self.th_11.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_12(self, port, baud):
        try:
            self.port_ch12 = Serial_comm(port=port, baud=baud)
            self.th_12 = Worker(self.port_ch12, parent=self)
            self.th_12.sec_changed.connect(self.time_update_12)

            self.pushButton_start_12.setEnabled(False)
            self.pushButton_stop_12.setEnabled(True)
            # Cal. Time & delta
            self.start_time_12 = datetime.now()
            self.end_time_12 = self.start_time_12 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_12_str = self.start_time_12.isoformat(timespec='seconds')
            self.end_time_12_str = self.end_time_12.isoformat(timespec='seconds')
            self.start_time_12_str = self.start_time_12_str.replace("T", ' ')
            self.end_time_12_str = self.end_time_12_str.replace("T", ' ')
            self.label_c12_2.setText(self.start_time_12_str)
            self.label_c12_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c12_3.setText(self.end_time_12_str)
            self.label_c12_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c12_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_12.start()
            self.th_12.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_13(self, port, baud):
        try:
            self.port_ch13 = Serial_comm(port=port, baud=baud)
            self.th_13 = Worker(self.port_ch13, parent=self)
            self.th_13.sec_changed.connect(self.time_update_13)

            self.pushButton_start_13.setEnabled(False)
            self.pushButton_stop_13.setEnabled(True)
            # Cal. Time & delta
            self.start_time_13 = datetime.now()
            self.end_time_13 = self.start_time_13 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_13_str = self.start_time_13.isoformat(timespec='seconds')
            self.end_time_13_str = self.end_time_13.isoformat(timespec='seconds')
            self.start_time_13_str = self.start_time_13_str.replace("T", ' ')
            self.end_time_13_str = self.end_time_13_str.replace("T", ' ')
            self.label_c13_2.setText(self.start_time_13_str)
            self.label_c13_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c13_3.setText(self.end_time_13_str)
            self.label_c13_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c13_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_13.start()
            self.th_13.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_14(self, port, baud):
        try:
            self.port_ch14 = Serial_comm(port=port, baud=baud)
            self.th_14 = Worker(self.port_ch14, parent=self)
            self.th_14.sec_changed.connect(self.time_update_14)

            self.pushButton_start_14.setEnabled(False)
            self.pushButton_stop_14.setEnabled(True)
            # Cal. Time & delta
            self.start_time_14 = datetime.now()
            self.end_time_14 = self.start_time_14 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_14_str = self.start_time_14.isoformat(timespec='seconds')
            self.end_time_14_str = self.end_time_14.isoformat(timespec='seconds')
            self.start_time_14_str = self.start_time_14_str.replace("T", ' ')
            self.end_time_14_str = self.end_time_14_str.replace("T", ' ')
            self.label_c14_2.setText(self.start_time_14_str)
            self.label_c14_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c14_3.setText(self.end_time_14_str)
            self.label_c14_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c14_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_14.start()
            self.th_14.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_15(self, port, baud):
        try:
            self.port_ch15 = Serial_comm(port=port, baud=baud)
            self.th_15 = Worker(self.port_ch15, parent=self)
            self.th_15.sec_changed.connect(self.time_update_15)

            self.pushButton_start_15.setEnabled(False)
            self.pushButton_stop_15.setEnabled(True)
            # Cal. Time & delta
            self.start_time_15 = datetime.now()
            self.end_time_15 = self.start_time_15 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_15_str = self.start_time_15.isoformat(timespec='seconds')
            self.end_time_15_str = self.end_time_15.isoformat(timespec='seconds')
            self.start_time_15_str = self.start_time_15_str.replace("T", ' ')
            self.end_time_15_str = self.end_time_15_str.replace("T", ' ')
            self.label_c15_2.setText(self.start_time_15_str)
            self.label_c15_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c15_3.setText(self.end_time_15_str)
            self.label_c15_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c15_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_15.start()
            self.th_15.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot()
    def time_start_16(self, port, baud):
        try:
            self.port_ch16 = Serial_comm(port=port, baud=baud)
            self.th_16 = Worker(self.port_ch16, parent=self)
            self.th_16.sec_changed.connect(self.time_update_16)
            self.pushButton_start_16.setEnabled(False)
            self.pushButton_stop_16.setEnabled(True)

            # Cal. Time & delta
            self.start_time_16 = datetime.now()
            self.end_time_16 = self.start_time_16 + relativedelta(hours=int(self.config['Setting']['durating_time']))
            self.start_time_16_str = self.start_time_16.isoformat(timespec='seconds')
            self.end_time_16_str = self.end_time_16.isoformat(timespec='seconds')
            self.start_time_16_str = self.start_time_16_str.replace("T", ' ')
            self.end_time_16_str = self.end_time_16_str.replace("T", ' ')
            self.label_c16_2.setText(self.start_time_16_str)
            self.label_c16_2.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c16_3.setText(self.end_time_16_str)
            self.label_c16_3.setStyleSheet("color:rgba(255, 180, 180, 210);")
            self.label_c16_4.setStyleSheet("image: url(:/img/svg/checkmark.svg);")

            self.th_16.start()
            self.th_16.working = True
        except:
            print("Could not open port : {}".format(port))
            msg = QtWidgets.QMessageBox()
            msg.setText("Serial Connect Error\nCould not open port : {}".format(port))
            msg.setWindowTitle("Serial Connect Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStyleSheet("")
            msg.exec_()
            pass

    @QtCore.pyqtSlot(list)
    def time_update(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time, now_time)
        duration_time = relativedelta(now_time, self.start_time)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[0][i] = self.df_bundle[0][i].append(df)
                self.df_bundle[0][i] = self.df_bundle[0][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()

        if int(delta_day.seconds) < 0:
            self.time_stop()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c1_1.setText(delta_day_str)
            self.label_c1_1.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_2(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_2, now_time)
        duration_time = relativedelta(now_time, self.start_time_2)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[1][i] = self.df_bundle[1][i].append(df)
                self.df_bundle[1][i] = self.df_bundle[1][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_2()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c2.setText(delta_day_str)
            self.label_c2.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_3(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_3, now_time)
        duration_time = relativedelta(now_time, self.start_time_3)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[2][i] = self.df_bundle[2][i].append(df)
                self.df_bundle[2][i] = self.df_bundle[2][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_3()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c3.setText(delta_day_str)
            self.label_c3.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_4(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_4, now_time)
        duration_time = relativedelta(now_time, self.start_time_4)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[3][i] = self.df_bundle[3][i].append(df)
                self.df_bundle[3][i] = self.df_bundle[3][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_4()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c4.setText(delta_day_str)
            self.label_c4.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_5(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_5, now_time)
        duration_time = relativedelta(now_time, self.start_time_5)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[4][i] = self.df_bundle[4][i].append(df)
                self.df_bundle[4][i] = self.df_bundle[4][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_5()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c5.setText(delta_day_str)
            self.label_c5.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_6(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_6, now_time)
        duration_time = relativedelta(now_time, self.start_time_6)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[5][i] = self.df_bundle[5][i].append(df)
                self.df_bundle[5][i] = self.df_bundle[5][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_6()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c6.setText(delta_day_str)
            self.label_c6.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_7(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_7, now_time)
        duration_time = relativedelta(now_time, self.start_time_7)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[6][i] = self.df_bundle[6][i].append(df)
                self.df_bundle[6][i] = self.df_bundle[6][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_7()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c7.setText(delta_day_str)
            self.label_c7.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_8(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_8, now_time)
        duration_time = relativedelta(now_time, self.start_time_8)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[7][i] = self.df_bundle[7][i].append(df)
                self.df_bundle[7][i] = self.df_bundle[7][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_8()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c8.setText(delta_day_str)
            self.label_c8.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_9(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_9, now_time)
        duration_time = relativedelta(now_time, self.start_time_9)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[8][i] = self.df_bundle[8][i].append(df)
                self.df_bundle[8][i] = self.df_bundle[8][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_9()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c9.setText(delta_day_str)
            self.label_c9.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_10(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_10, now_time)
        duration_time = relativedelta(now_time, self.start_time_10)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[9][i] = self.df_bundle[9][i].append(df)
                self.df_bundle[9][i] = self.df_bundle[9][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_10()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c10.setText(delta_day_str)
            self.label_c10.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_11(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_11, now_time)
        duration_time = relativedelta(now_time, self.start_time_11)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[10][i] = self.df_bundle[10][i].append(df)
                self.df_bundle[10][i] = self.df_bundle[10][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_11()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c11.setText(delta_day_str)
            self.label_c11.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_12(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_12, now_time)
        duration_time = relativedelta(now_time, self.start_time_12)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[11][i] = self.df_bundle[11][i].append(df)
                self.df_bundle[11][i] = self.df_bundle[11][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_12()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c12.setText(delta_day_str)
            self.label_c12.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_13(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_13, now_time)
        duration_time = relativedelta(now_time, self.start_time_13)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[12][i] = self.df_bundle[12][i].append(df)
                self.df_bundle[12][i] = self.df_bundle[12][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_13()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c13.setText(delta_day_str)
            self.label_c13.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_14(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_14, now_time)
        duration_time = relativedelta(now_time, self.start_time_14)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[13][i] = self.df_bundle[13][i].append(df)
                self.df_bundle[13][i] = self.df_bundle[13][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_14()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c14.setText(delta_day_str)
            self.label_c14.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_15(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_15, now_time)
        duration_time = relativedelta(now_time, self.start_time_15)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[14][i] = self.df_bundle[14][i].append(df)
                self.df_bundle[14][i] = self.df_bundle[14][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_15()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c15.setText(delta_day_str)
            self.label_c15.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot(list)
    def time_update_16(self, msg):
        now_time = datetime.now()
        delta_day = relativedelta(self.end_time_16, now_time)
        duration_time = relativedelta(now_time, self.start_time_16)
        duration_time_sec = duration_time.days * 60 * 60 * 24 \
                            + duration_time.hours * 60 * 60 \
                            + duration_time.minutes * 60 \
                            + duration_time.seconds + 1
        # Data read & draw plot
        time_interval = int(self.config['Setting']['time_interval'])
        if (int(delta_day.minutes) % time_interval == 0) and (int(delta_day.seconds) == 0):
            list_msg = self.hex_to_dec(msg)
            print(self.hex_to_dec(msg))
            for i in range(16):
                df = self.df_update(duration_time_sec, index_no=i, list_msg=list_msg)
                self.df_bundle[15][i] = self.df_bundle[15][i].append(df)
                self.df_bundle[15][i] = self.df_bundle[15][i].reset_index(drop=True)
            t = threading.Thread(target=self.plot_update, args=())
            t.daemon = True
            t.start()
        if int(delta_day.seconds) < 0:
            self.time_stop_16()
        else:
            delta_day_str = "{}d {}h {}m {}s".format(delta_day.days, delta_day.hours, delta_day.minutes,
                                                     delta_day.seconds)
            self.label_c16.setText(delta_day_str)
            self.label_c16.setStyleSheet("color:rgba(255, 180, 180, 210);")

    @QtCore.pyqtSlot()
    def time_stop(self):
        self.port_ch.serial_close()
        self.th.working = False

        self.pushButton_start.setEnabled(True)
        self.pushButton_stop.setEnabled(False)
        self.label_c1_1.setStyleSheet("")
        self.label_c1_2.setStyleSheet("")
        self.label_c1_3.setStyleSheet("")
        self.label_c1_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch1'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch01_{}.xlsx'.format(mkdir_path, file_name, self.start_time_str.replace(' ', '').replace(':', '').replace('-','')[8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch1[i].to_excel(writer, sheet_name='No {}'.format(i+1), index=False)

        for i in range(16):
            self.df_ch1[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1), self.start_time_str.replace(' ', '').replace(':', '').replace('-','')[8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_2(self):
        self.port_ch2.serial_close()
        self.th_2.working = False

        self.pushButton_start_2.setEnabled(True)
        self.pushButton_stop_2.setEnabled(False)
        self.label_c2.setStyleSheet("")
        self.label_c2_2.setStyleSheet("")
        self.label_c2_3.setStyleSheet("")
        self.label_c2_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_2_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch2'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch02_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch2[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch2[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_2_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_3(self):
        self.th_3.working = False

        self.pushButton_start_3.setEnabled(True)
        self.pushButton_stop_3.setEnabled(False)
        self.label_c3.setStyleSheet("")
        self.label_c3_2.setStyleSheet("")
        self.label_c3_3.setStyleSheet("")
        self.label_c3_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_3_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch3'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch03_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch3[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch3[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_3_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_4(self):
        self.th_4.working = False

        self.pushButton_start_4.setEnabled(True)
        self.pushButton_stop_4.setEnabled(False)
        self.label_c4.setStyleSheet("")
        self.label_c4_2.setStyleSheet("")
        self.label_c4_3.setStyleSheet("")
        self.label_c4_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_4_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch4'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch04_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch4[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch4[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_4_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_5(self):
        self.th_5.working = False

        self.pushButton_start_5.setEnabled(True)
        self.pushButton_stop_5.setEnabled(False)
        self.label_c5.setStyleSheet("")
        self.label_c5_2.setStyleSheet("")
        self.label_c5_3.setStyleSheet("")
        self.label_c5_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_5_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch5'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch05_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch5[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch5[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_5_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_6(self):
        self.th_6.working = False

        self.pushButton_start_6.setEnabled(True)
        self.pushButton_stop_6.setEnabled(False)
        self.label_c6.setStyleSheet("")
        self.label_c6_2.setStyleSheet("")
        self.label_c6_3.setStyleSheet("")
        self.label_c6_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_6_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch6'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch06_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch6[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch6[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_6_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_7(self):
        self.th_7.working = False

        self.pushButton_start_7.setEnabled(True)
        self.pushButton_stop_7.setEnabled(False)
        self.label_c7.setStyleSheet("")
        self.label_c7_2.setStyleSheet("")
        self.label_c7_3.setStyleSheet("")
        self.label_c7_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_7_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch7'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch07_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch7[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch7[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_7_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_8(self):
        self.th_8.working = False

        self.pushButton_start_8.setEnabled(True)
        self.pushButton_stop_8.setEnabled(False)
        self.label_c8.setStyleSheet("")
        self.label_c8_2.setStyleSheet("")
        self.label_c8_3.setStyleSheet("")
        self.label_c8_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_8_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch8'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch08_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch8[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch8[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_8_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)


    @QtCore.pyqtSlot()
    def time_stop_9(self):
        self.th_9.working = False

        self.pushButton_start_9.setEnabled(True)
        self.pushButton_stop_9.setEnabled(False)
        self.label_c9.setStyleSheet("")
        self.label_c9_2.setStyleSheet("")
        self.label_c9_3.setStyleSheet("")
        self.label_c9_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")
        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_9_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch9'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch09_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch9[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch9[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_9_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_10(self):
        self.th_10.working = False

        self.pushButton_start_10.setEnabled(True)
        self.pushButton_stop_10.setEnabled(False)
        self.label_c10.setStyleSheet("")
        self.label_c10_2.setStyleSheet("")
        self.label_c10_3.setStyleSheet("")
        self.label_c10_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_10_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch10'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch10_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch10[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch10[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_10_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_11(self):
        self.th_11.working = False

        self.pushButton_start_11.setEnabled(True)
        self.pushButton_stop_11.setEnabled(False)
        self.label_c11.setStyleSheet("")
        self.label_c11_2.setStyleSheet("")
        self.label_c11_3.setStyleSheet("")
        self.label_c11_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_11_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch11'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch011_{}.xlsx'.format(mkdir_path, file_name,
        #                                          self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                          8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch11[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch11[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_11_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_12(self):
        self.th_12.working = False

        self.pushButton_start_12.setEnabled(True)
        self.pushButton_stop_12.setEnabled(False)
        self.label_c12.setStyleSheet("")
        self.label_c12_2.setStyleSheet("")
        self.label_c12_3.setStyleSheet("")
        self.label_c12_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_12_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch12'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch012_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch12[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch12[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_12_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_13(self):
        self.th_13.working = False

        self.pushButton_start_13.setEnabled(True)
        self.pushButton_stop_13.setEnabled(False)
        self.label_c13.setStyleSheet("")
        self.label_c13_2.setStyleSheet("")
        self.label_c13_3.setStyleSheet("")
        self.label_c13_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_13_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch13'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch013_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch13[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch13[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_13_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_14(self):
        self.th_14.working = False

        self.pushButton_start_14.setEnabled(True)
        self.pushButton_stop_14.setEnabled(False)
        self.label_c14.setStyleSheet("")
        self.label_c14_2.setStyleSheet("")
        self.label_c14_3.setStyleSheet("")
        self.label_c14_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_14_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch14'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch14_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch14[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch14[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_14_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_15(self):
        self.th_15.working = False

        self.pushButton_start_15.setEnabled(True)
        self.pushButton_stop_15.setEnabled(False)
        self.label_c15.setStyleSheet("")
        self.label_c15_2.setStyleSheet("")
        self.label_c15_3.setStyleSheet("")
        self.label_c15_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_15_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch15'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch15_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch15[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch15[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_15_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    @QtCore.pyqtSlot()
    def time_stop_16(self):
        self.th_16.working = False

        self.pushButton_start_16.setEnabled(True)
        self.pushButton_stop_16.setEnabled(False)
        self.label_c16.setStyleSheet("")
        self.label_c16_2.setStyleSheet("")
        self.label_c16_3.setStyleSheet("")
        self.label_c16_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);")

        path = self.config['Setting']['save_folder_path']
        file_name = self.config['Setting']['file_name']
        mkdir_path = '{}/{}'.format(path, self.start_time_16_str.split(' ')[0])
        mkdir_path = mkdir_path + '/Ch16'
        try:
            os.mkdir(mkdir_path)
        except OSError as error:
            print('Already exists : {}'.format(mkdir_path))
            pass
        # xlxs_path = '{}/{}_ch16_{}.xlsx'.format(mkdir_path, file_name,
        #                                         self.start_time_str.replace(' ', '').replace(':', '').replace('-', '')[
        #                                         8:])
        # with pd.ExcelWriter(xlxs_path) as writer:
        #     for i in range(16):
        #         self.df_ch16[i].to_excel(writer, sheet_name='No {}'.format(i + 1), index=False)
        for i in range(16):
            self.df_ch16[i].to_csv(
                '{}/{}_no{}_{}.csv'.format(mkdir_path, file_name, (i + 1),
                                               self.start_time_16_str.replace(' ', '').replace(':', '').replace('-', '')[
                                               8:]),
                index=False)

    # Page move func.
    def btn_menu_1(self):
        self.label.setText(':: Home')
        self.btn_select_style(0)
        self.stackedWidget.setCurrentIndex(0)

    def btn_menu_2(self):
        self.label.setText(':: Home >> MPD')
        self.btn_select_style(1)
        self.stackedWidget.setCurrentIndex(1)

    def btn_menu_3(self):
        self.label.setText(':: Home >> Thermistor')
        self.btn_select_style(2)
        self.stackedWidget.setCurrentIndex(2)

    def btn_menu_4(self):
        self.label.setText(':: Home >> TEC Voltage')
        self.btn_select_style(3)
        self.stackedWidget.setCurrentIndex(3)

    def btn_menu_5(self):
        self.label.setText(':: Home >> TEC Current')
        self.btn_select_style(4)
        self.stackedWidget.setCurrentIndex(4)

    def btn_menu_6(self):
        self.label.setText(':: Home >> LD Voltage')
        self.btn_select_style(5)
        self.stackedWidget.setCurrentIndex(5)

    def btn_menu_7(self):
        self.label.setText(':: Home >> LD Current')
        self.btn_select_style(6)
        self.stackedWidget.setCurrentIndex(6)

    def btn_menu_8(self):
        self.label.setText(':: Setting')
        self.btn_select_style(7)
        self.stackedWidget.setCurrentIndex(7)

    def btn_select_style(self, index_no):
        self.btn_home.setStyleSheet("")
        self.btn_mpd.setStyleSheet("")
        self.btn_ther.setStyleSheet("")
        self.btn_tec_volt.setStyleSheet("")
        self.btn_tec_curr.setStyleSheet("")
        self.btn_ld_volt.setStyleSheet("")
        self.btn_ld_curr.setStyleSheet("")
        self.btn_setting.setStyleSheet("")
        if index_no == 0:
            self.btn_home.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 1:
            self.btn_mpd.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 2:
            self.btn_ther.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 3:
            self.btn_tec_volt.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 4:
            self.btn_tec_curr.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 5:
            self.btn_ld_volt.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 6:
            self.btn_ld_curr.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")
        elif index_no == 7:
            self.btn_setting.setStyleSheet("background-color: #36393F;color:rgba(255, 255, 255, 210);")

    # plot draw
    def plot_mpd(self, title, x_data, y_data):
        self.widget_3.axes.cla()
        self.widget_3.axes.set_title(title)
        self.widget_3.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_3.axes.set_ylabel(r"Current (uA)")
        self.widget_3.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_3.axes.tick_params(axis="x", direction="in", pad=10)
        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_3.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_3.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        # self.widget_3.axes.get_figure().tight_layout()
        self.widget_3.draw()

    def plot_thrm(self, title, x_data, y_data):
        self.widget_4.axes.cla()
        self.widget_4.axes.set_title(title)
        self.widget_4.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_4.axes.set_ylabel(r"Temperature (deg.)")
        self.widget_4.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_4.axes.tick_params(axis="x", direction="in", pad=10)
        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_4.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_4.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        self.widget_4.draw()

    def plot_tec_volt(self, title, x_data, y_data):
        self.widget_5.axes.cla()
        self.widget_5.axes.set_title(title)
        self.widget_5.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_5.axes.set_ylabel(r"Voltage (mV)")
        self.widget_5.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_5.axes.tick_params(axis="x", direction="in", pad=10)

        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_5.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_5.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        self.widget_5.draw()

    def plot_tec_curr(self, title, x_data, y_data):
        self.widget_6.axes.cla()
        self.widget_6.axes.set_title(title)
        self.widget_6.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_6.axes.set_ylabel(r"Current (mA)")
        self.widget_6.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_6.axes.tick_params(axis="x", direction="in", pad=10)
        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_6.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_6.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        self.widget_6.draw()

    def plot_ld_volt(self, title, x_data, y_data):
        self.widget_7.axes.cla()
        self.widget_7.axes.set_title(title)
        self.widget_7.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_7.axes.set_ylabel(r"Voltage (mV)")
        self.widget_7.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_7.axes.tick_params(axis="x", direction="in", pad=10)

        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_7.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_7.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        self.widget_7.draw()

    def plot_ld_curr(self, title, x_data, y_data):
        self.widget_8.axes.cla()
        self.widget_8.axes.set_title(title)
        self.widget_8.axes.set_xlabel(r"Duration Time (hr)")
        self.widget_8.axes.set_ylabel(r"Current (mA)")
        self.widget_8.axes.tick_params(axis="y", direction="in", pad=10)
        self.widget_8.axes.tick_params(axis="x", direction="in", pad=10)

        if x_data:
            linestyles = ['-', '--', '-.', ':']
            for i in range(16):
                self.widget_8.axes.plot(x_data[i], y_data[i], ms=100, lw=1, linestyle=linestyles[int(i / 4)],
                                        label='No. {}'.format((i + 1)))
            self.widget_8.axes.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)
        else:
            pass
        self.widget_8.draw()

    def file_dialog_tfo(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './', 'Excel File (*.xlsx)')
        if not fname:
            self.lineEdit_st_4.setText(self.config['Setting']['template_file_open'])
        else:
            self.lineEdit_st_4.setText(fname)

    def file_dialog_sf(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open File', './')
        if not fname:
            self.lineEdit_st_5.setText(self.config['Setting']['save_folder_path'])
        else:
            self.lineEdit_st_5.setText(fname)

    def save_setting(self):
        self.config['Setting']['durating_time'] = self.lineEdit_st.text()
        self.config['Setting']['file_name'] = self.lineEdit_st_2.text()
        self.config['Setting']['operator'] = self.lineEdit_st_3.text()
        self.config['Setting']['template_file_open'] = self.lineEdit_st_4.text()
        self.config['Setting']['save_folder_path'] = self.lineEdit_st_5.text()
        self.config['Setting']['time_interval'] = self.lineEdit_st_7.text()

        with open('setting.ini', 'w', encoding='UTF-8') as configfile:
            self.config.write(configfile)

    def restore_setting(self):
        self.config.read('setting.ini', "utf8")
        self.lineEdit_st.setText(self.config['Setting']['durating_time'])
        self.lineEdit_st_2.setText(self.config['Setting']['file_name'])
        self.lineEdit_st_3.setText(self.config['Setting']['operator'])
        self.lineEdit_st_4.setText(self.config['Setting']['template_file_open'])
        self.lineEdit_st_5.setText(self.config['Setting']['save_folder_path'])

    # draggable windows
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def init_state_btn(self):
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop_2.setEnabled(False)
        self.pushButton_stop_3.setEnabled(False)
        self.pushButton_stop_4.setEnabled(False)
        self.pushButton_stop_5.setEnabled(False)
        self.pushButton_stop_6.setEnabled(False)
        self.pushButton_stop_7.setEnabled(False)
        self.pushButton_stop_8.setEnabled(False)
        self.pushButton_stop_9.setEnabled(False)
        self.pushButton_stop_10.setEnabled(False)
        self.pushButton_stop_11.setEnabled(False)
        self.pushButton_stop_12.setEnabled(False)
        self.pushButton_stop_13.setEnabled(False)
        self.pushButton_stop_14.setEnabled(False)
        self.pushButton_stop_15.setEnabled(False)
        self.pushButton_stop_16.setEnabled(False)


class Worker(QtCore.QThread):
    sec_changed = QtCore.pyqtSignal(list)

    def __init__(self, port_ch, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        self.sec = sec

        # Serial Port connect
        self.port_ch = port_ch
        # self.port_ch = Serial_comm(port, baud)
        # self.port_ch1 = Serial_comm('COM4', 38400)

        self.config = configparser.ConfigParser()
        self.config.read('setting.ini', "utf8")
        self.time_interval = int(self.config['Setting']['time_interval'])

    ''' Runtime error !!
    def __del__(self):
        print(".... end thread.....")
        self.wait()
    '''

    def run(self):
        while self.working:
            if self.port_ch != '':
                if self.sec % (self.time_interval * 60) - (self.time_interval * 60 - 60) == 0:
                    self.port_ch.wh_data('1')
                getVal = self.port_ch.df
            else:
                getVal = list(self.sec)
            self.sec_changed.emit(getVal)
            self.sleep(1)
            self.sec += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    form.show()
    # plot update
    form.btn_plot_test('mpd_ch1')
    form.btn_plot_test('them_ch1')
    form.btn_plot_test('tv_ch1')
    form.btn_plot_test('tc_ch1')
    form.btn_plot_test('ldv_ch1')
    form.btn_plot_test('ldc_ch1')
    sys.exit(app.exec_())
