#
#   This is the JTAG IDCODE  Look Up tool for USD devices
#       Program Name:               jlookup.py
#       Program Version Number:     1.0
#       Author(s):                  ab@merimetso.net
#       Date:                       31st October 2020
#
#
import sys
#
#
#
#

def usage():
    print("\nProgram: jlookup.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21")
    print("")
    print("USAGE: jlookup.py [-h] [-t bin|dec|hex] IDCODE")
    print("")
    print(" Optional Arguments:")
    print("    -h    Show this help message and exit.")
    print("    -t    The type of the JTAG IDCode. The type as are follows.")
    print("             bin - The IDCODE is expressed as a binary number.")
    print("             dec - The IDCODE is expressed as a decimal number.")
    print("             hex - The IDCODE is expressed as a hexidecimal number.")
    print("         If the -t option is NOT specified it id assumed that the IDCODE is")
    print("         expressed as a hexidecimal number.")
    print('')
    print('EXAMPLE:')
    print('        $ python jlookup.py -t hex 0x4caf0477 ')
    print("")
    sys.exit(1)


#
#
#
#

def m_member(arg_list, member):
    counter = 0
    for _ in arg_list:
        if arg_list[counter] == member:
            return True, counter
        counter = counter + 1
    return False, -1


#
#
#
#

def j_lookup(number, d_type):
    hex_Val = 0x00000000
    int_Val = 0
    bin_Val = bin(int_Val)
    print("\nProgram: jlookup.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21\n")
    if d_type == "hex":
        hex_Val = number
        int_Val = int(number, 16)
        bin_Val = bin(int_Val)
    #
    if d_type == "dec":
        int_Val = number
        hex_Val = hex(int(number))
        bin_Val = bin(int(int_Val))
    #
    if d_type == "bin":
        bin_Val = number
        hex_Val = hex(int(bin_Val, 2))
    #
    idcodestr = "00000000000000000000000000000000" + str(bin_Val)[2:]
    idlen = len(idcodestr)
    idcode = idcodestr[:idlen - 1]
    idcode = idcode[idlen - 32:idlen + 1]
    vn = idcode[0:4]
    pid = idcode[4:20]
    mid = idcode[20:32]
    print('The IDCODE is := ' + idcode + "1" + " / " + hex_Val)
    print(' -> The Manufacturer ID is : ' + str(mid) + " / " + hex(int(mid, 2)) + ' ( ' + jtag_dict[mid][0] + ' ) ')
    print(' -> The Part ID is         : ' + str(pid) + " / " + hex(int(pid, 2)))
    print(' -> The Version Number is  : ' + str(vn) + " / " + hex(int(vn, 2)))
    print('')


#
#
#

if __name__ == "__main__":
    #
    data_Type = "hex"
    jtag_dict = {'00000000001': ('AMD',), '00000000010': ('AMI',), '00000000011': ('Fairchild',),
                 '00000000100': ('Fujitsu',), '00000000101': ('GTE',), '00000000110': ('Harris',),
                 '00000000111': ('Hitachi',), '00000001000': ('Inmos',), '00000001001': ('Intel',),
                 '00000001010': ('I.T.T.',), '00000001011': ('Intersil',), '00000001100': ('Monolithic Memories',),
                 '00000001101': ('Mostek',), '00000001110': ('Freescale (Motorola)',), '00000001111': ('National',),
                 '00000010000': ('NEC',), '00000010001': ('RCA',), '00000010010': ('Raytheon',),
                 '00000010011': ('Conexant (Rockwell)',), '00000010100': ('Seeq',), '00000010101': ('NXP (Philips)',),
                 '00000010110': ('Synertek',), '00000010111': ('Texas Instruments',), '00000011000': ('Toshiba',),
                 '00000011001': ('Xicor',), '00000011010': ('Zilog',), '00000011011': ('Eurotechnique',),
                 '00000011100': ('Mitsubishi',), '00000011101': ('Lucent (AT&T)',), '00000011110': ('Exel',),
                 '00000011111': ('Atmel',), '00000100000': ('SGS/Thomson',), '00000100001': ('Lattice Semi.',),
                 '00000100010': ('NCR',), '00000100011': ('Wafer Scale Integration',), '00000100100': ('IBM',),
                 '00000100101': ('Tristar',), '00000100110': ('Visic',), '00000100111': ('Intl. CMOS Technology',),
                 '00000101000': ('SSSI',), '00000101001': ('MicrochipTechnology',), '00000101010': ('Ricoh Ltd.',),
                 '00000101011': ('VLSI',), '00000101100': ('Micron Technology',),
                 '00000101101': ('Hynix Semiconductor (Hyundai Electronics)',), '00000101110': ('OKI Semiconductor',),
                 '00000101111': ('ACTEL',), '00000110000': ('Sharp',), '00000110001': ('Catalyst',),
                 '00000110010': ('Panasonic',), '00000110011': ('IDT',), '00000110100': ('Cypress',),
                 '00000110101': ('DEC',), '00000110110': ('LSI Logic',), '00000110111': ('Zarlink (Plessey)',),
                 '00000111000': ('UTMC',), '00000111001': ('Thinking Machine',), '00000111010': ('Thomson CSF',),
                 '00000111011': ('Integrated CMOS (Vertex)',), '00000111100': ('Honeywell',),
                 '00000111101': ('Tektronix',), '00000111110': ('Oracle Corporation',),
                 '00000111111': ('Silicon Storage Technology',), '00001000000': ('ProMos/Mosel Vitelic',),
                 '00001000001': ('Infineon (Siemens)',), '00001000010': ('Macronix',), '00001000011': ('Xerox',),
                 '00001000100': ('Plus Logic',), '00001000101': ('SanDisk Corporation',),
                 '00001000110': ('Elan Circuit Tech.',), '00001000111': ('European Silicon Str.',),
                 '00001001000': ('Apple Computer',), '00001001001': ('Xilinx',), '00001001010': ('Compaq',),
                 '00001001011': ('Protocol Engines',), '00001001100': ('SCI',), '00001001101': ('Seiko Instruments',),
                 '00001001110': ('Samsung',), '00001001111': ('I3 Design System',), '00001010000': ('Klic',),
                 '00001010001': ('Crosspoint Solutions',), '00001010010': ('Alliance Semiconductor',),
                 '00001010011': ('Tandem',), '00001010100': ('Hewlett-Packard',),
                 '00001010101': ('Integrated Silicon Solutions',), '00001010110': ('Brooktree',),
                 '00001010111': ('New Media',), '00001011000': ('MHS Electronic',),
                 '00001011001': ('Performance Semi.',), '00001011010': ('Winbond Electronic',),
                 '00001011011': ('Kawasaki Steel',), '00001011100': ('Bright Micro',), '00001011101': ('TECMAR',),
                 '00001011110': ('Exar',), '00001011111': ('PCMCIA',), '00001100000': ('LG Semi (Goldstar)',),
                 '00001100001': ('Northern Telecom',), '00001100010': ('Sanyo',),
                 '00001100011': ('Array Microsystems',), '00001100100': ('Crystal Semiconductor',),
                 '00001100101': ('Analog Devices',), '00001100110': ('PMC-Sierra',), '00001100111': ('Asparix',),
                 '00001101000': ('Convex Computer',), '00001101001': ('Quality Semiconductor',),
                 '00001101010': ('Nimbus Technology',), '00001101011': ('Transwitch',),
                 '00001101100': ('Micronas (ITT Intermetall)',), '00001101101': ('Cannon',), '00001101110': ('Altera',),
                 '00001101111': ('NEXCOM',), '00001110000': ('QUALCOMM',), '00001110001': ('Sony',),
                 '00001110010': ('Cray Research',), '00001110011': ('AMS(Austria Micro)',), '00001110100': ('Vitesse',),
                 '00001110101': ('Aster Electronics',), '00001110110': ('Bay Networks (Synoptic)',),
                 '00001110111': ('Zentrum/ZMD',), '00001111000': ('TRW',), '00001111001': ('Thesys',),
                 '00001111010': ('Solbourne Computer',), '00001111011': ('Allied-Signal',),
                 '00001111100': ('Dialog Semiconductor',), '00001111101': ('Media Vision',),
                 '00001111110': ('Numonyx Corporation',), '00010000001': ('Cirrus Logic',),
                 '00010000010': ('National Instruments',), '00010000011': ('ILC Data Device',),
                 '00010000100': ('Alcatel Mietec',), '00010000101': ('Micro Linear',), '00010000110': ('Univ. of NC',),
                 '00010000111': ('JTAG Technologies',), '00010001000': ('BAE Systems (Loral)',),
                 '00010001001': ('Nchip',), '00010001010': ('Galileo Tech',), '00010001011': ('Bestlink Systems',),
                 '00010001100': ('Graychip',), '00010001101': ('GENNUM',), '00010001110': ('VideoLogic',),
                 '00010001111': ('Robert Bosch',), '00010010000': ('Chip Express',), '00010010001': ('DATARAM',),
                 '00010010010': ('United Microelectronics Corp.',), '00010010011': ('TCSI',),
                 '00010010100': ('Smart Modular',), '00010010101': ('Hughes Aircraft',),
                 '00010010110': ('Lanstar Semiconductor',), '00010010111': ('Qlogic',), '00010011000': ('Kingston',),
                 '00010011001': ('Music Semi',), '00010011010': ('Ericsson Components',), '00010011011': ('SpaSE',),
                 '00010011100': ('Eon Silicon Devices',), '00010011101': ('Programmable Micro Corp',),
                 '00010011110': ('DoD',), '00010011111': ('Integ. Memories Tech.',), '00010100000': ('Corollary Inc.',),
                 '00010100001': ('Dallas Semiconductor',), '00010100010': ('Omnivision',),
                 '00010100011': ('EIV(Switzerland)',), '00010100100': ('Novatel Wireless',),
                 '00010100101': ('Zarlink (Mitel)',), '00010100110': ('Clearpoint',), '00010100111': ('Cabletron',),
                 '00010101000': ('STEC (Silicon Tech)',), '00010101001': ('Vanguard',),
                 '00010101010': ('Hagiwara Sys-Com',), '00010101011': ('Vantis',), '00010101100': ('Celestica',),
                 '00010101101': ('Century',), '00010101110': ('Hal Computers',), '00010101111': ('Rohm Company Ltd.',),
                 '00010110000': ('Juniper Networks',), '00010110001': ('Libit Signal Processing',),
                 '00010110010': ('Mushkin Enhanced Memory',), '00010110011': ('Tundra Semiconductor',),
                 '00010110100': ('Adaptec Inc.',), '00010110101': ('LightSpeed Semi.',), '00010110110': ('ZSP Corp.',),
                 '00010110111': ('AMIC Technology',), '00010111000': ('Adobe Systems',), '00010111001': ('Dynachip',),
                 '00010111010': ('PNY Electronics',), '00010111011': ('Newport Digital',),
                 '00010111100': ('MMC Networks',), '00010111101': ('T Square',), '00010111110': ('Seiko Epson',),
                 '00010111111': ('Broadcom',), '00011000000': ('Viking Components',),
                 '00011000001': ('V3 Semiconductor',), '00011000010': ('Flextronics (Orbit Semiconductor)',),
                 '00011000011': ('Suwa Electronics',), '00011000100': ('Transmeta',), '00011000101': ('Micron CMS',),
                 '00011000110': ('American Computer & Digital Components Inc',), '00011000111': ('Enhance 3000 Inc',),
                 '00011001000': ('Tower Semiconductor',), '00011001001': ('CPU Design',),
                 '00011001010': ('Price Point',), '00011001011': ('Maxim Integrated Product',),
                 '00011001100': ('Tellabs',), '00011001101': ('Centaur Technology',),
                 '00011001110': ('Unigen Corporation',), '00011001111': ('Transcend Information',),
                 '00011010000': ('Memory Card Technology',), '00011010001': ('CKD Corporation Ltd.',),
                 '00011010010': ('Capital Instruments, Inc.',), '00011010011': ('Aica Kogyo, Ltd.',),
                 '00011010100': ('Linvex Technology',), '00011010101': ('MSC Vertriebs GmbH',),
                 '00011010110': ('AKM Company, Ltd.',), '00011010111': ('Dynamem, Inc.',), '00011011000': ('NERA ASA',),
                 '00011011001': ('GSI Technology',), '00011011010': ('Dane-Elec (C Memory)',),
                 '00011011011': ('Acorn Computers',), '00011011100': ('Lara Technology',),
                 '00011011101': ('Oak Technology, Inc.',), '00011011110': ('Itec Memory',),
                 '00011011111': ('Tanisys Technology',), '00011100000': ('Truevision',),
                 '00011100001': ('Wintec Industries',), '00011100010': ('Super PC Memory',),
                 '00011100011': ('MGV Memory',), '00011100100': ('Galvantech',), '00011100101': ('Gadzoox Networks',),
                 '00011100110': ('Multi Dimensional Cons.',), '00011100111': ('GateField',),
                 '00011101000': ('Integrated Memory System',), '00011101001': ('Triscend',), '00011101010': ('XaQti',),
                 '00011101011': ('Goldenram',), '00011101100': ('Clear Logic',),
                 '00011101101': ('Cimaron Communications',), '00011101110': ('Nippon Steel Semi. Corp.',),
                 '00011101111': ('Advantage Memory',), '00011110000': ('AMCC',), '00011110001': ('LeCroy',),
                 '00011110010': ('Yamaha Corporation',), '00011110011': ('Digital Microwave',),
                 '00011110100': ('NetLogic Microsystems',), '00011110101': ('MIMOS Semiconductor',),
                 '00011110110': ('Advanced Fibre',), '00011110111': ('BF Goodrich Data.',), '00011111000': ('Epigram',),
                 '00011111001': ('Acbel Polytech Inc.',), '00011111010': ('Apacer Technology',),
                 '00011111011': ('Admor Memory',), '00011111100': ('FOXCONN',),
                 '00011111101': ('Quadratics Superconductor',), '00011111110': ('3COM',),
                 '00100000001': ('Camintonn Corporation',), '00100000010': ('ISOA Incorporated',),
                 '00100000011': ('Agate Semiconductor',), '00100000100': ('ADMtek Incorporated',),
                 '00100000101': ('HYPERTEC',), '00100000110': ('Adhoc Technologies',),
                 '00100000111': ('MOSAID Technologies',), '00100001000': ('Ardent Technologies',),
                 '00100001001': ('Switchcore',), '00100001010': ('Cisco Systems, Inc.',),
                 '00100001011': ('Allayer Technologies',), '00100001100': ('WorkX AG (Wichman)',),
                 '00100001101': ('Oasis Semiconductor',), '00100001110': ('Novanet Semiconductor',),
                 '00100001111': ('E-M Solutions',), '00100010000': ('Power General',),
                 '00100010001': ('Advanced Hardware Arch.',), '00100010010': ('Inova Semiconductors GmbH',),
                 '00100010011': ('Telocity',), '00100010100': ('Delkin Devices',),
                 '00100010101': ('Symagery Microsystems',), '00100010110': ('C-Port Corporation',),
                 '00100010111': ('SiberCore Technologies',), '00100011000': ('Southland Microsystems',),
                 '00100011001': ('Malleable Technologies',), '00100011010': ('Kendin Communications',),
                 '00100011011': ('Great Technology Microcomputer',), '00100011100': ('Sanmina Corporation',),
                 '00100011101': ('HADCO Corporation',), '00100011110': ('Corsair',),
                 '00100011111': ('Actrans System Inc.',), '00100100000': ('ALPHA Technologies',),
                 '00100100001': ('Silicon Laboratories, Inc. (Cygnal)',), '00100100010': ('Artesyn Technologies',),
                 '00100100011': ('Align Manufacturing',), '00100100100': ('Peregrine Semiconductor',),
                 '00100100101': ('Chameleon Systems',), '00100100110': ('Aplus Flash Technology',),
                 '00100100111': ('MIPS Technologies',), '00100101000': ('Chrysalis ITS',),
                 '00100101001': ('ADTEC Corporation',), '00100101010': ('Kentron Technologies',),
                 '00100101011': ('Win Technologies',), '00100101100': ('Tachyon Semiconductor (ASIC)',),
                 '00100101101': ('Extreme Packet Devices',), '00100101110': ('RF Micro Devices',),
                 '00100101111': ('Siemens AG',), '00100110000': ('Sarnoff Corporation',),
                 '00100110001': ('Itautec SA',), '00100110010': ('Radiata Inc.',),
                 '00100110011': ('Benchmark Elect. (AVEX)',), '00100110100': ('Legend',),
                 '00100110101': ('SpecTek Incorporated',), '00100110110': ('Hi/fn',),
                 '00100110111': ('Enikia Incorporated',), '00100111000': ('SwitchOn Networks',),
                 '00100111001': ('AANetcom Incorporated',), '00100111010': ('Micro Memory Bank',),
                 '00100111011': ('ESS Technology',), '00100111100': ('Virata Corporation',),
                 '00100111101': ('Excess Bandwidth',), '00100111110': ('West Bay Semiconductor',),
                 '00100111111': ('DSP Group',), '00101000000': ('Newport Communications',),
                 '00101000001': ('Chip2Chip Incorporated',), '00101000010': ('Phobos Corporation',),
                 '00101000011': ('Intellitech Corporation',), '00101000100': ('Nordic VLSI ASA',),
                 '00101000101': ('Ishoni Networks',), '00101000110': ('Silicon Spice',),
                 '00101000111': ('Alchemy Semiconductor',), '00101001000': ('Agilent Technologies',),
                 '00101001001': ('Centillium Communications',), '00101001010': ('W.L. Gore',),
                 '00101001011': ('HanBit Electronics',), '00101001100': ('GlobeSpan',), '00101001101': ('Element 14',),
                 '00101001110': ('Pycon',), '00101001111': ('Saifun Semiconductors',),
                 '00101010000': ('Sibyte, Incorporated',), '00101010001': ('MetaLink Technologies',),
                 '00101010010': ('Feiya Technology',), '00101010011': ('I & C Technology',),
                 '00101010100': ('Shikatronics',), '00101010101': ('Elektrobit',), '00101010110': ('Megic',),
                 '00101010111': ('Com-Tier',), '00101011000': ('Malaysia Micro Solutions',),
                 '00101011001': ('Hyperchip',), '00101011010': ('Gemstone Communications',),
                 '00101011011': ('Anadigm (Anadyne)',), '00101011100': ('3ParData',),
                 '00101011101': ('Mellanox Technologies',), '00101011110': ('Tenx Technologies',),
                 '00101011111': ('Helix AG',), '00101100000': ('Domosys',), '00101100001': ('Skyup Technology',),
                 '00101100010': ('HiNT Corporation',), '00101100011': ('Chiaro',),
                 '00101100100': ('MDT Technologies GmbH',), '00101100101': ('Exbit Technology A/S',),
                 '00101100110': ('Integrated Technology Express',), '00101100111': ('AVED Memory',),
                 '00101101000': ('Legerity',), '00101101001': ('Jasmine Networks',),
                 '00101101010': ('Caspian Networks',), '00101101011': ('nCUBE',),
                 '00101101100': ('Silicon Access Networks',), '00101101101': ('FDK Corporation',),
                 '00101101110': ('High Bandwidth Access',), '00101101111': ('MultiLink Technology',),
                 '00101110000': ('BRECIS',), '00101110001': ('World Wide Packets',), '00101110010': ('APW',),
                 '00101110011': ('Chicory Systems',), '00101110100': ('Xstream Logic',), '00101110101': ('Fast-Chip',),
                 '00101110110': ('Zucotto Wireless',), '00101110111': ('Realchip',), '00101111000': ('Galaxy Power',),
                 '00101111001': ('eSilicon',), '00101111010': ('Morphics Technology',),
                 '00101111011': ('Accelerant Networks',), '00101111100': ('Silicon Wave',),
                 '00101111101': ('SandCraft',), '00101111110': ('Elpida',), '00110000001': ('Solectron',),
                 '00110000010': ('Optosys Technologies',), '00110000011': ('Buffalo (Formerly Melco)',),
                 '00110000100': ('TriMedia Technologies',), '00110000101': ('Cyan Technologies',),
                 '00110000110': ('Global Locate',), '00110000111': ('Optillion',),
                 '00110001000': ('Terago Communications',), '00110001001': ('Ikanos Communications',),
                 '00110001010': ('Princeton Technology',), '00110001011': ('Nanya Technology',),
                 '00110001100': ('Elite Flash Storage',), '00110001101': ('Mysticom',),
                 '00110001110': ('LightSand Communications',), '00110001111': ('ATI Technologies',),
                 '00110010000': ('Agere Systems',), '00110010001': ('NeoMagic',), '00110010010': ('AuroraNetics',),
                 '00110010011': ('Golden Empire',), '00110010100': ('Mushkin',), '00110010101': ('Tioga Technologies',),
                 '00110010110': ('Netlist',), '00110010111': ('TeraLogic',), '00110011000': ('Cicada Semiconductor',),
                 '00110011001': ('Centon Electronics',), '00110011010': ('Tyco Electronics',),
                 '00110011011': ('Magis Works',), '00110011100': ('Zettacom',),
                 '00110011101': ('Cogency Semiconductor',), '00110011110': ('Chipcon AS',),
                 '00110011111': ('Aspex Technology',), '00110100000': ('F5 Networks',),
                 '00110100001': ('Programmable Silicon Solutions',), '00110100010': ('ChipWrights',),
                 '00110100011': ('Acorn Networks',), '00110100100': ('Quicklogic',),
                 '00110100101': ('Kingmax Semiconductor',), '00110100110': ('BOPS',), '00110100111': ('Flasys',),
                 '00110101000': ('BitBlitz Communications',), '00110101001': ('eMemory Technology',),
                 '00110101010': ('Procket Networks',), '00110101011': ('Purple Ray',),
                 '00110101100': ('Trebia Networks',), '00110101101': ('Delta Electronics',),
                 '00110101110': ('Onex Communications',), '00110101111': ('Ample Communications',),
                 '00110110000': ('Memory Experts Intl',), '00110110001': ('Astute Networks',),
                 '00110110010': ('Azanda Network Devices',), '00110110011': ('Dibcom',), '00110110100': ('Tekmos',),
                 '00110110101': ('API NetWorks',), '00110110110': ('Bay Microsystems',),
                 '00110110111': ('Firecron Ltd',), '00110111000': ('Resonext Communications',),
                 '00110111001': ('Tachys Technologies',), '00110111010': ('Equator Technology',),
                 '00110111011': ('Concept Computer',), '00110111100': ('SILCOM',), '00110111101': ('3Dlabs',),
                 '00110111110': ('ct Magazine',), '00110111111': ('Sanera Systems',),
                 '00111000000': ('Silicon Packets',), '00111000001': ('Viasystems Group',), '00111000010': ('Simtek',),
                 '00111000011': ('Semicon Devices Singapore',), '00111000100': ('Satron Handelsges',),
                 '00111000101': ('Improv Systems',), '00111000110': ('INDUSYS GmbH',), '00111000111': ('Corrent',),
                 '00111001000': ('Infrant Technologies',), '00111001001': ('Ritek Corp',),
                 '00111001010': ('empowerTel Networks',), '00111001011': ('Hypertec',),
                 '00111001100': ('Cavium Networks',), '00111001101': ('PLX Technology',),
                 '00111001110': ('Massana Design',), '00111001111': ('Intrinsity',),
                 '00111010000': ('Valence Semiconductor',), '00111010001': ('Terawave Communications',),
                 '00111010010': ('IceFyre Semiconductor',), '00111010011': ('Primarion',),
                 '00111010100': ('Picochip Designs Ltd',), '00111010101': ('Silverback Systems',),
                 '00111010110': ('Jade Star Technologies',), '00111010111': ('Pijnenburg Securealink',),
                 '00111011000': ('takeMS International AG',), '00111011001': ('Cambridge Silicon Radio',),
                 '00111011010': ('Swissbit',), '00111011011': ('Nazomi Communications',),
                 '00111011100': ('eWave System',), '00111011101': ('Rockwell Collins',),
                 '00111011110': ('Picocel Co. Ltd. (Paion)',), '00111011111': ('Alphamosaic Ltd',),
                 '00111100000': ('Sandburst',), '00111100001': ('SiCon Video',), '00111100010': ('NanoAmp Solutions',),
                 '00111100011': ('Ericsson Technology',), '00111100100': ('PrairieComm',),
                 '00111100101': ('Mitac International',), '00111100110': ('Layer N Networks',),
                 '00111100111': ('MtekVision (Atsana)',), '00111101000': ('Allegro Networks',),
                 '00111101001': ('Marvell Semiconductors',), '00111101010': ('Netergy Microelectronic',),
                 '00111101011': ('NVIDIA',), '00111101100': ('Internet Machines',),
                 '00111101101': ('Peak Electronics',), '00111101110': ('Litchfield Communication',),
                 '00111101111': ('Accton Technology',), '00111110000': ('Teradiant Networks',),
                 '00111110001': ('Scaleo Chip',), '00111110010': ('Cortina Systems',),
                 '00111110011': ('RAM Components',), '00111110100': ('Raqia Networks',), '00111110101': ('ClearSpeed',),
                 '00111110110': ('Matsushita Battery',), '00111110111': ('Xelerated',), '00111111000': ('SimpleTech',),
                 '00111111001': ('Utron Technology',), '00111111010': ('Astec International',),
                 '00111111011': ('AVM gmbH',), '00111111100': ('Redux Communications',),
                 '00111111101': ('Dot Hill Systems',), '00111111110': ('TeraChip',),
                 '01000000001': ('T-RAM Incorporated',), '01000000010': ('Innovics Wireless',),
                 '01000000011': ('Teknovus',), '01000000100': ('KeyEye Communications',),
                 '01000000101': ('Runcom Technologies',), '01000000110': ('RedSwitch',), '01000000111': ('Dotcast',),
                 '01000001000': ('Silicon Mountain Memory',), '01000001001': ('Signia Technologies',),
                 '01000001010': ('Pixim',), '01000001011': ('Galazar Networks',),
                 '01000001100': ('White Electronic Designs',), '01000001101': ('Patriot Scientific',),
                 '01000001110': ('Neoaxiom Corporation',), '01000001111': ('3Y Power Technology',),
                 '01000010000': ('Scaleo Chip',), '01000010001': ('Potentia Power Systems',),
                 '01000010010': ('C-guys Incorporated',),
                 '01000010011': ('Digital Communications Technology Incorporated',),
                 '01000010100': ('Silicon-Based Technology',), '01000010101': ('Fulcrum Microsystems',),
                 '01000010110': ('Positivo Informatica Ltd',), '01000010111': ('XIOtech Corporation',),
                 '01000011000': ('PortalPlayer',), '01000011001': ('Zhiying Software',),
                 '01000011010': ('ParkerVision, Inc.',), '01000011011': ('Phonex Broadband',),
                 '01000011100': ('Skyworks Solutions',), '01000011101': ('Entropic Communications',),
                 '01000011110': ('Pacific Force Technology',), '01000011111': ('Zensys A/S',),
                 '01000100000': ('Legend Silicon Corp.',), '01000100001': ('Sci-worx GmbH',),
                 '01000100010': ('SMSC (Standard Microsystems)',), '01000100011': ('Renesas Electronics',),
                 '01000100100': ('Raza Microelectronics',), '01000100101': ('Phyworks',), '01000100110': ('MediaTek',),
                 '01000100111': ('Non-cents Productions',), '01000101000': ('US Modular',),
                 '01000101001': ('Wintegra Ltd.',), '01000101010': ('Mathstar',), '01000101011': ('StarCore',),
                 '01000101100': ('Oplus Technologies',), '01000101101': ('Mindspeed',),
                 '01000101110': ('Just Young Computer',), '01000101111': ('Radia Communications',),
                 '01000110000': ('OCZ',), '01000110001': ('Emuzed',), '01000110010': ('LOGIC Devices',),
                 '01000110011': ('Inphi Corporation',), '01000110100': ('Quake Technologies',),
                 '01000110101': ('Vixel',), '01000110110': ('SolusTek',), '01000110111': ('Kongsberg Maritime',),
                 '01000111000': ('Faraday Technology',), '01000111001': ('Altium Ltd.',), '01000111010': ('Insyte',),
                 '01000111011': ('ARM Ltd.',), '01000111100': ('DigiVision',), '01000111101': ('Vativ Technologies',),
                 '01000111110': ('Endicott Interconnect Technologies',), '01000111111': ('Pericom',),
                 '01001000000': ('Bandspeed',), '01001000001': ('LeWiz Communications',),
                 '01001000010': ('CPU Technology',), '01001000011': ('Ramaxel Technology',),
                 '01001000100': ('DSP Group',), '01001000101': ('Axis Communications',),
                 '01001000110': ('Legacy Electronics',), '01001000111': ('Chrontel',),
                 '01001001000': ('Powerchip Semiconductor',), '01001001001': ('MobilEye Technologies',),
                 '01001001010': ('Excel Semiconductor',), '01001001011': ('A-DATA Technology',),
                 '01001001100': ('VirtualDigm',), '01001001101': ('G Skill Intl',), '01001001110': ('Quanta Computer',),
                 '01001001111': ('Yield Microelectronics',), '01001010000': ('Afa Technologies',),
                 '01001010001': ('KINGBOX Technology Co. Ltd.',), '01001010010': ('Ceva',),
                 '01001010011': ('iStor Networks',), '01001010100': ('Advance Modules',), '01001010101': ('Microsoft',),
                 '01001010110': ('Open-Silicon',), '01001010111': ('Goal Semiconductor',),
                 '01001011000': ('ARC International',), '01001011001': ('Simmtec',), '01001011010': ('Metanoia',),
                 '01001011011': ('Key Stream',), '01001011100': ('Lowrance Electronics',), '01001011101': ('Adimos',),
                 '01001011110': ('SiGe Semiconductor',), '01001011111': ('Fodus Communications',),
                 '01001100000': ('Credence Systems Corp.',), '01001100001': ('Genesis Microchip Inc.',),
                 '01001100010': ('Vihana, Inc.',), '01001100011': ('WIS Technologies',),
                 '01001100100': ('GateChange Technologies',), '01001100101': ('High Density Devices AS',),
                 '01001100110': ('Synopsys',), '01001100111': ('Gigaram',),
                 '01001101000': ('Enigma Semiconductor Inc.',), '01001101001': ('Century Micro Inc.',),
                 '01001101010': ('Icera Semiconductor',), '01001101011': ('Mediaworks Integrated Systems',),
                 '01001101100': ('Oâ€™Neil Product Development',), '01001101101': ('Supreme Top Technology Ltd.',),
                 '01001101110': ('MicroDisplay Corporation',), '01001101111': ('Team Group Inc.',),
                 '01001110000': ('Sinett Corporation',), '01001110001': ('Toshiba Corporation',),
                 '01001110010': ('Tensilica',), '01001110011': ('SiRF Technology',), '01001110100': ('Bacoc Inc.',),
                 '01001110101': ('SMaL Camera Technologies',), '01001110110': ('Thomson SC',),
                 '01001110111': ('Airgo Networks',), '01001111000': ('Wisair Ltd.',), '01001111001': ('SigmaTel',),
                 '01001111010': ('Arkados',), '01001111011': ('Compete IT gmbH Co. KG',),
                 '01001111100': ('Eudar Technology Inc.',), '01001111101': ('Focus Enhancements',),
                 '01001111110': ('Xyratex',), '01010000001': ('Specular Networks',),
                 '01010000010': ('Patriot Memory (PDP Systems)',), '01010000011': ('U-Chip Technology Corp.',),
                 '01010000100': ('Silicon Optix',), '01010000101': ('Greenfield Networks',),
                 '01010000110': ('CompuRAM GmbH',), '01010000111': ('Stargen, Inc.',),
                 '01010001000': ('NetCell Corporation',), '01010001001': ('Excalibrus Technologies Ltd',),
                 '01010001010': ('SCM Microsystems',), '01010001011': ('Xsigo Systems, Inc.',),
                 '01010001100': ('CHIPS & Systems Inc',), '01010001101': ('Tier 1 Multichip Solutions',),
                 '01010001110': ('CWRL Labs',), '01010001111': ('Teradici',), '01010010000': ('Gigaram, Inc.',),
                 '01010010001': ('g2 Microsystems',), '01010010010': ('PowerFlash Semiconductor',),
                 '01010010011': ('P.A. Semi, Inc.',), '01010010100': ('NovaTech Solutions, S.A.',),
                 '01010010101': ('c2 Microsystems, Inc.',), '01010010110': ('Level5 Networks',),
                 '01010010111': ('COS Memory AG',), '01010011000': ('Innovasic Semiconductor',),
                 '01010011001': ('02IC Co. Ltd',), '01010011010': ('Tabula, Inc.',),
                 '01010011011': ('Crucial Technology',), '01010011100': ('Chelsio Communications',),
                 '01010011101': ('Solarflare Communications',), '01010011110': ('Xambala Inc.',),
                 '01010011111': ('EADS Astrium',), '01010100000': ('Terra Semiconductor, Inc.',),
                 '01010100001': ('Imaging Works, Inc.',), '01010100010': ('Astute Networks, Inc.',),
                 '01010100011': ('Tzero',), '01010100100': ('Emulex',), '01010100101': ('Power-One',),
                 '01010100110': ('Pulse~LINK Inc.',), '01010100111': ('Hon Hai Precision Industry',),
                 '01010101000': ('White Rock Networks Inc.',), '01010101001': ('Telegent Systems USA, Inc.',),
                 '01010101010': ('Atrua Technologies, Inc.',), '01010101011': ('Acbel Polytech Inc.',),
                 '01010101100': ('eRide Inc.',), '01010101101': ('ULi Electronics Inc.',),
                 '01010101110': ('Magnum Semiconductor Inc.',), '01010101111': ('neoOne Technology, Inc.',),
                 '01010110000': ('Connex Technology, Inc.',), '01010110001': ('Stream Processors, Inc.',),
                 '01010110010': ('Focus Enhancements',), '01010110011': ('Telecis Wireless, Inc.',),
                 '01010110100': ('uNav Microelectronics',), '01010110101': ('Tarari, Inc.',),
                 '01010110110': ('Ambric, Inc.',), '01010110111': ('Newport Media, Inc.',), '01010111000': ('VMTS',),
                 '01010111001': ('Enuclia Semiconductor, Inc.',), '01010111010': ('Virtium Technology Inc.',),
                 '01010111011': ('Solid State System Co., Ltd.',), '01010111100': ('Kian Tech LLC',),
                 '01010111101': ('Artimi',), '01010111110': ('Power Quotient International',),
                 '01010111111': ('Avago Technologies',), '01011000000': ('ADTechnology',),
                 '01011000001': ('Sigma Designs',), '01011000010': ('SiCortex, Inc.',),
                 '01011000011': ('Ventura Technology Group',), '01011000100': ('eASIC',),
                 '01011000101': ('M.H.S. SAS',), '01011000110': ('Micro Star International',),
                 '01011000111': ('Rapport Inc.',), '01011001000': ('Makway International',),
                 '01011001001': ('Broad Reach Engineering Co.',), '01011001010': ('Semiconductor Mfg Intl Corp',),
                 '01011001011': ('SiConnect',), '01011001100': ('FCI USA Inc.',), '01011001101': ('Validity Sensors',),
                 '01011001110': ('Coney Technology Co. Ltd.',), '01011001111': ('Spans Logic',),
                 '01011010000': ('Neterion Inc.',), '01011010001': ('Qimonda',),
                 '01011010010': ('New Japan Radio Co. Ltd.',), '01011010011': ('Velogix',),
                 '01011010100': ('Montalvo Systems',), '01011010101': ('iVivity Inc.',),
                 '01011010110': ('Walton Chaintech',), '01011010111': ('AENEON',),
                 '01011011000': ('Lorom Industrial Co. Ltd.',), '01011011001': ('Radiospire Networks',),
                 '01011011010': ('Sensio Technologies, Inc.',), '01011011011': ('Nethra Imaging',),
                 '01011011100': ('Hexon Technology Pte Ltd',), '01011011101': ('CompuStocx (CSX)',),
                 '01011011110': ('Methode Electronics, Inc.',), '01011011111': ('Connect One Ltd.',),
                 '01011100000': ('Opulan Technologies',), '01011100001': ('Septentrio NV',),
                 '01011100010': ('Goldenmars Technology Inc.',), '01011100011': ('Kreton Corporation',),
                 '01011100100': ('Cochlear Ltd.',), '01011100101': ('Altair Semiconductor',),
                 '01011100110': ('NetEffect, Inc.',), '01011100111': ('Spansion, Inc.',),
                 '01011101000': ('Taiwan Semiconductor Mfg',), '01011101001': ('Emphany Systems Inc.',),
                 '01011101010': ('ApaceWave Technologies',), '01011101011': ('Mobilygen Corporation',),
                 '01011101100': ('Tego',), '01011101101': ('Cswitch Corporation',),
                 '01011101110': ('Haier (Beijing) IC Design Co.',), '01011101111': ('MetaRAM',),
                 '01011110000': ('Axel Electronics Co. Ltd.',), '01011110001': ('Tilera Corporation',),
                 '01011110010': ('Aquantia',), '01011110011': ('Vivace Semiconductor',),
                 '01011110100': ('Redpine Signals',), '01011110101': ('Octalica',),
                 '01011110110': ('InterDigital Communications',), '01011110111': ('Avant Technology',),
                 '01011111000': ('Asrock, Inc.',), '01011111001': ('Availink',), '01011111010': ('Quartics, Inc.',),
                 '01011111011': ('Element CXI',), '01011111100': ('Innovaciones Microelectronicas',),
                 '01011111101': ('VeriSilicon Microelectronics',), '01011111110': ('W5 Networks',),
                 '01100000001': ('MOVEKING',), '01100000010': ('Mavrix Technology, Inc.',),
                 '01100000011': ('CellGuide Ltd.',), '01100000100': ('Faraday Technology',),
                 '01100000101': ('Diablo Technologies, Inc.',), '01100000110': ('Jennic',), '01100000111': ('Octasic',),
                 '01100001000': ('Molex Incorporated',), '01100001001': ('3Leaf Networks',),
                 '01100001010': ('Bright Micron Technology',), '01100001011': ('Netxen',),
                 '01100001100': ('NextWave Broadband Inc.',), '01100001101': ('DisplayLink',),
                 '01100001110': ('ZMOS Technology',), '01100001111': ('Tec-Hill',), '01100010000': ('Multigig, Inc.',),
                 '01100010001': ('Amimon',), '01100010010': ('Euphonic Technologies, Inc.',),
                 '01100010011': ('BRN Phoenix',), '01100010100': ('InSilica',), '01100010101': ('Ember Corporation',),
                 '01100010110': ('Avexir Technologies Corporation',), '01100010111': ('Echelon Corporation',),
                 '01100011000': ('Edgewater Computer Systems',), '01100011001': ('XMOS Semiconductor Ltd.',),
                 '01100011010': ('GENUSION, Inc.',), '01100011011': ('Memory Corp NV',),
                 '01100011100': ('SiliconBlue Technologies',), '01100011101': ('Rambus Inc.',),
                 '01100011110': ('Andes Technology Corporation',), '01100011111': ('Coronis Systems',),
                 '01100100000': ('Achronix Semiconductor',), '01100100001': ('Siano Mobile Silicon Ltd.',),
                 '01100100010': ('Semtech Corporation',), '01100100011': ('Pixelworks Inc.',),
                 '01100100100': ('Gaisler Research AB',), '01100100101': ('Teranetics',),
                 '01100100110': ('Toppan Printing Co. Ltd.',), '01100100111': ('Kingxcon',),
                 '01100101000': ('Silicon Integrated Systems',), '01100101001': ('I-O Data Device, Inc.',),
                 '01100101010': ('NDS Americas Inc.',), '01100101011': ('Solomon Systech Limited',),
                 '01100101100': ('On Demand Microelectronics',), '01100101101': ('Amicus Wireless Inc.',),
                 '01100101110': ('SMARDTV SNC',), '01100101111': ('Comsys Communication Ltd.',),
                 '01100110000': ('Movidia Ltd.',), '01100110001': ('Javad GNSS, Inc.',),
                 '01100110010': ('Montage Technology Group',), '01100110011': ('Trident Microsystems',),
                 '01100110100': ('Super Talent',), '01100110101': ('Optichron, Inc.',),
                 '01100110110': ('Future Waves UK Ltd.',), '01100110111': ('SiBEAM, Inc.',),
                 '01100111000': ('Inicore,Inc.',), '01100111001': ('Virident Systems',),
                 '01100111010': ('M2000, Inc.',), '01100111011': ('ZeroG Wireless, Inc.',),
                 '01100111100': ('Gingle Technology Co. Ltd.',), '01100111101': ('Space Micro Inc.',),
                 '01100111110': ('Wilocity',), '01100111111': ('Novafora, Ic.',), '01101000000': ('iKoa Corporation',),
                 '01101000001': ('ASint Technology',), '01101000010': ('Ramtron',),
                 '01101000011': ('Plato Networks Inc.',), '01101000100': ('IPtronics AS',),
                 '01101000101': ('Infinite-Memories',), '01101000110': ('Parade Technologies Inc.',),
                 '01101000111': ('Dune Networks',), '01101001000': ('GigaDevice Semiconductor',),
                 '01101001001': ('Modu Ltd.',), '01101001010': ('CEITEC',), '01101001011': ('Northrop Grumman',),
                 '01101001100': ('XRONET Corporation',), '01101001101': ('Sicon Semiconductor AB',),
                 '01101001110': ('Atla Electronics Co. Ltd.',), '01101001111': ('TOPRAM Technology',),
                 '01101010000': ('Silego Technology Inc.',), '01101010001': ('Kinglife',),
                 '01101010010': ('Ability Industries Ltd.',),
                 '01101010011': ('Silicon Power Computer & Communications',),
                 '01101010100': ('Augusta Technology, Inc.',), '01101010101': ('Nantronics Semiconductors',),
                 '01101010110': ('Hilscher Gesellschaft',), '01101010111': ('Quixant Ltd.',),
                 '01101011000': ('Percello Ltd.',), '01101011001': ('NextIO Inc.',),
                 '01101011010': ('Scanimetrics Inc.',), '01101011011': ('FS-Semi Company Ltd.',),
                 '01101011100': ('Infinera Corporation',), '01101011101': ('SandForce Inc.',),
                 '01101011110': ('Lexar Media',), '01101011111': ('Teradyne Inc.',),
                 '01101100000': ('Memory Exchange Corp.',), '01101100001': ('Suzhou Smartek Electronics',),
                 '01101100010': ('Avantium Corporation',), '01101100011': ('ATP Electronics Inc.',),
                 '01101100100': ('Valens Semiconductor Ltd',), '01101100101': ('Agate Logic, Inc.',),
                 '01101100110': ('Netronome',), '01101100111': ('Zenverge, Inc.',), '01101101000': ('N-trig Ltd',),
                 '01101101001': ('SanMax Technologies Inc.',), '01101101010': ('Contour Semiconductor Inc.',),
                 '01101101011': ('TwinMOS',), '01101101100': ('Silicon Systems, Inc.',),
                 '01101101101': ('V-Color Technology Inc.',), '01101101110': ('Certicom Corporation',),
                 '01101101111': ('JSC ICC Milandr',), '01101110000': ('PhotoFast Global Inc.',),
                 '01101110001': ('InnoDisk Corporation',), '01101110010': ('Muscle Power',),
                 '01101110011': ('Energy Micro',), '01101110100': ('Innofidei',),
                 '01101110101': ('CopperGate Communications',), '01101110110': ('Holtek Semiconductor Inc.',),
                 '01101110111': ('Myson Century, Inc.',), '01101111000': ('FIDELIX',),
                 '01101111001': ('Red Digital Cinema',), '01101111010': ('Densbits Technology',),
                 '01101111011': ('Zempro',), '01101111100': ('MoSys',), '01101111101': ('Provigent',),
                 '01101111110': ('Triad Semiconductor, Inc.',), '01110000001': ('Siklu Communication Ltd.',),
                 '01110000010': ('A Force Manufacturing Ltd.',), '01110000011': ('Strontium',),
                 '01110000100': ('Abilis Systems',), '01110000101': ('Siglead, Inc.',),
                 '01110000110': ('Ubicom, Inc.',), '01110000111': ('Unifosa Corporation',),
                 '01110001000': ('Stretch, Inc.',), '01110001001': ('Lantiq Deutschland GmbH',),
                 '01110001010': ('Visipro.',), '01110001011': ('EKMemory',),
                 '01110001100': ('Microelectronics Institute ZTE',), '01110001101': ('Cognovo Ltd.',),
                 '01110001110': ('Carry Technology Co. Ltd.',), '01110001111': ('Nokia',),
                 '01110010000': ('King Tiger Technology',), '01110010001': ('Sierra Wireless',),
                 '01110010010': ('HT Micron',), '01110010011': ('Albatron Technology Co. Ltd.',),
                 '01110010100': ('Leica Geosystems AG',), '01110010101': ('BroadLight',), '01110010110': ('AEXEA',),
                 '01110010111': ('ClariPhy Communications, Inc.',), '01110011000': ('Green Plug',),
                 '01110011001': ('Design Art Networks',), '01110011010': ('Mach Xtreme Technology Ltd.',),
                 '01110011011': ('ATO Solutions Co. Ltd.',), '01110011100': ('Ramsta',),
                 '01110011101': ('Greenliant Systems, Ltd.',), '01110011110': ('Teikon',),
                 '01110011111': ('Antec Hadron',), '01110100000': ('NavCom Technology, Inc.',),
                 '01110100001': ('Shanghai Fudan Microelectronics',), '01110100010': ('Calxeda, Inc.',),
                 '01110100011': ('JSC EDC Electronics',), '01110100100': ('Kandit Technology Co. Ltd.',),
                 '01110100101': ('Ramos Technology',), '01110100110': ('Goldenmars Technology',),
                 '01110100111': ('XeL Technology Inc.',), '01110101000': ('Newzone Corporation',),
                 '01110101001': ('ShenZhen MercyPower Tech',), '01110101010': ('Nanjing Yihuo Technology.',),
                 '01110101011': ('Nethra Imaging Inc.',), '01110101100': ('SiTel Semiconductor BV',),
                 '01110101101': ('SolidGear Corporation',), '01110101110': ('Topower Computer Ind Co Ltd.',),
                 '01110101111': ('Wilocity',), '01110110000': ('Profichip GmbH',),
                 '01110110001': ('Gerad Technologies',), '01110110010': ('Ritek Corporation',),
                 '01110110011': ('Gomos Technology Limited',), '01110110100': ('Memoright Corporation',),
                 '01110110101': ('D-Broad, Inc.',), '01110110110': ('HiSilicon Technologies',),
                 '01110110111': ('Syndiant Inc..',), '01110111000': ('Enverv Inc.',), '01110111001': ('Cognex',),
                 '01110111010': ('Xinnova Technology Inc.',), '01110111011': ('Ultron AG',),
                 '01110111100': ('Concord Idea Corporation',), '01110111101': ('AIM Corporation',),
                 '01110111110': ('Lifetime Memory Products',), '01110111111': ('Ramsway',),
                 '01111000000': ('Recore Systems B.V.',), '01111000001': ('Haotian Jinshibo Science Tech',),
                 '01111000010': ('Being Advanced Memory',), '01111000011': ('Adesto Technologies',),
                 '01111000100': ('Giantec Semiconductor, Inc.',), '01111000101': ('HMD Electronics AG',),
                 '01111000110': ('Gloway International (HK)',), '01111000111': ('Kingcore',),
                 '01111001000': ('Anucell Technology Holding',),
                 '01111001001': ('Accord Software & Systems Pvt. Ltd.',), '01111001010': ('Active-Semi Inc.',),
                 '01111001011': 'Denso Corporation'}
    #
    try:
        memTruth, index = m_member(sys.argv, '-h')
        if memTruth:
            usage()
            sys.exit(0)
    except:
        sys.exit(0)
    #
    try:
        memTruth, index = m_member(sys.argv, '-t')
        if memTruth:
            sys.argv.pop(index)
            dataInput = sys.argv.pop(index)
            if dataInput == "bin":
                data_Type = "bin"
            elif dataInput == "dec":
                data_Type = "dec"
            elif dataInput == "hex":
                data_Type = "hex"
            else:
                print("ERROR: Error processing ICODE number type - Please refer to the following:\n")
                usage()
                sys.exit(0)
    except:
        print('ERROR: Error processing the "-t" argument in the command line.')
        sys.exit(0)
    #
    try:
        if sys.argv[0] == 'jlookup.py':
            sys.argv.pop(0)
        if len(sys.argv) == 1:
            j_lookup(sys.argv.pop(0), data_Type)
            sys.exit(1)
        else:
            print('ERROR: There is an illegal parameter in the command line.')
            print('       If you need to see the help page then use the "-h" option.\n')
            sys.exit(0)
    except:
        sys.exit(0)
#
#
#
#
#
