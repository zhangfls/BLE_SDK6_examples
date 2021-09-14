## Example description

This example shows:

- Create MIDI service on BLE peripheral side as [BLE-MIDI specification](https://www.midi.org/specifications-old/item/bluetooth-le-midi) required.
- Demonstrate playing note on an iOS APP that supports MIDI profile, by pressing the buttons on the DA1458x Pro Development kit.
- The example can be downloaded from [Here](http://lpccs-docs.dialog-semiconductor.com/SW_Example/SDK6/DA14531-DA14585-586_BLE-Midi.zip)

You can watch this intro video:

   <div style="text-align:center">
      <video width="800" height="400" controls>
         <source src="midi.mp4" type="video/mp4">
         Your browser does not support this tag!
      </video>
   <p><b><i>Demonstration of Dialog SmartBond™ DA14531 Module BLE Midi</i></b></p>   
   </div> 

## HW and SW configuration

- **Hardware configuration**

- This example runs on the DA14531 and DA14585/586 Bluetooth Smart SoC devices.
- The DA145xxDEVKT-P PRO-Motherboard with jumper setting for SPI flash programming. The user manuals for the development kits can be found [Here](https://www.dialog-semiconductor.com/products/da14531-development-kit-pro) for the DA145xxDEVKT-P PRO-Motherboard.

- For the DA14531 getting started guide you can refer to this [LINK](http://lpccs-docs.dialog-semiconductor.com/UM-B-117-DA14531-Getting-Started-With-The-Pro-Development-Kit/index.html)
- For the DA14531 Module getting started guide you can refer to this [LINK](http://lpccs-docs.dialog-semiconductor.com/UM-B-139-Getting-Started-with-DA14531-TINY-Module/index.html)
- For the DA14585/586 getting started guide you can refer to this [LINK](http://lpccs-docs.dialog-semiconductor.com/da14585_getting_started/index.html).

The example is running from SRAM. To run the program from flash please visit chapter 17 of the [SmartSnippets Toolbox User Manual](http://lpccs-docs.dialog-semiconductor.com/UM-B-083/tools/mkImage.html)

* __Hardware configuration DA14531 using DA145xxDEVKT-P PRO-Motherboard__

	- SW2 (button 2) is configured to P0_11, located on J19 (red box)
	- Connect the DA145xxDEVKT-P PRO-Motherboard to the working station through USB1 connector. 

	![Motherboard_Hardware_Configuration_DA14531](assets/Motherboard_Hardware_Configuration_DA14531.png)
	
* **Hardware configuration DA14585 using the DA145xxDEVKT-P PRO-Motherboard**

	- SW3 (button 3) is configured to P1_1, located on J19 (red box)
	- Connect the DA145xxDEVKT-P PRO-Motherboard to the working station through USB1 connector.

	![Motherboard_Hardware_Configuration_DA14585](assets/Motherboard_Hardware_Configuration_DA14585.png)
	
- **Software configuration**
    - [SDK6.0.14](https://www.dialog-semiconductor.com/da14531_sdk_latest)
    - **SEGGER’s J-Link** tools should be downloaded and installed.
    - An iOS smartphone with a MIDI app (for example **KORG Module**).

## How to run the example

### Initial Setup

- Before launching the Keil project, make sure to link the SDK and project environment using the Python linker script `dlg_make_keil_vx.xxx`. More information [Here](http://lpccs-docs.dialog-semiconductor.com/Software_Example_Setup/index.html).


### Compile & Run

- Navigate to ``project_environment`` folder and open the Keil project.
- Compile and then launch the example. 
- To verify please open **KORG Module** app:

    1. Open Settings page and tap the Scan button

        ![settings](assets/settings.png)

    2. Find the device named **DIALOG-MIDI** and connect to it.

        ![finddevice](assets/finddevice.png)

    3. Pair the device

        ![pair](assets/pair.png)

    4. Press the button on the dev-kit to play the note.

        ![playnote](assets/playnote.png)


## Known Limitations


- There are No known limitations for this example. But you can check and refer to the following application note for
[DA14585 known hardware limitations](https://www.dialog-semiconductor.com/sites/default/files/da1458x-knownlimitations_2019_01_07.pdf)
- Refer to the following application note for DA14531 known [hardware limitations](https://www.dialog-semiconductor.com/da14531_HW_Limitation)
- Also refer to Dialog Software [Forum Link](https://support.dialog-semiconductor.com/forum)

## License


**************************************************************************************

 Copyright (c) 2020 Dialog Semiconductor. All rights reserved.

 This software ("Software") is owned by Dialog Semiconductor. By using this Software
 you agree that Dialog Semiconductor retains all intellectual property and proprietary
 rights in and to this Software and any use, reproduction, disclosure or distribution
 of the Software without express written permission or a license agreement from Dialog
 Semiconductor is strictly prohibited. This Software is solely for use on or in
 conjunction with Dialog Semiconductor products.

 EXCEPT AS OTHERWISE PROVIDED IN A LICENSE AGREEMENT BETWEEN THE PARTIES OR AS
 REQUIRED BY LAW, THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. EXCEPT AS OTHERWISE PROVIDED
 IN A LICENSE AGREEMENT BETWEEN THE PARTIES OR BY LAW, IN NO EVENT SHALL DIALOG
 SEMICONDUCTOR BE LIABLE FOR ANY DIRECT, SPECIAL, INDIRECT, INCIDENTAL, OR
 CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
 PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
 ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THE SOFTWARE.

**************************************************************************************