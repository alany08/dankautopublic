#!EMOJI IS ONLY FOR PLS WORK

def checkdig():
                unfinished!!! the rest is copied alr lmao
                elif "match the color" in latest.text.lower():
                    #Match the color to whatever idk
                    print("Match the color minigame!")
                    words = driver.find_element_by_id(latest_id).find_elements_by_tag_name("code")
                    words_final = []
                    for word in words:
                        words_final.append(word.text)
                    words = words_final
                    colors = driver.find_element_by_id(latest_id).find_elements_by_tag_name("img")
                    colors_final = []
                    for color in colors:
                        colors_final.append(color.get_attribute("aria-label"))
                    colors = colors_final
                    if not len(words) == len(colors):
                        raise ValueError("Error while matching color: More/Less words than colors!")
                    memorized = {}
                    for i in range(0, len(colors)):
                        memorized.update(words[i]: colors[i])
                    print("Grabbed data: \n" + str(memorized))
                    old_txt = latest.text
                    starttime = time.time()
                    while True:
                        if not (time.time() - starttime) > 15:
                            latest = driver.find_element_by_id(latest_id)
                            if not latest.text == old_txt:
                                break
                        else:
                            print("Timed out waiting for text change...")
                            break

def checkwork():
    try:
        parent = driver.find_elements_by_css_selector(".messageContent-")
        prompt = driver
#no need to copy highlow code, this doesn't use embeds so it wont work
#You can base the dunk the ball code offkk ok
    except:
        pass

"""
memorize words
<div
    class="message-2CShn3 cozyMessage-1DWF9U groupStart-3Mlgv1 wrapper-30-Nkg cozy-VmLDNB zalgo-26OfGz"
    role="article"
    data-list-item-id="chat-messages___chat-messages-933149185031692388"
    tabindex="-1"
    aria-setsize="-1"
    aria-roledescription="Message"
    aria-labelledby="message-username-933149185031692388 uid_1 message-content-933149185031692388 uid_2 message-timestamp-933149185031692388"
    aria-describedby=""
>
    <div class="contents-2MsGLg">
        <img src="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=128" aria-hidden="true" class="avatar-2e8lTP clickable-31pE3P" alt=" " />
        <h2 class="header-2jRmjb" aria-describedby="reply-context-933149185031692388" aria-labelledby="message-username-933149185031692388 message-timestamp-933149185031692388">
            <span id="message-username-933149185031692388" class="headerText-2z4IhQ">
                <span class="username-h_Y3Us desaturateUserColors-1O-G89 clickable-31pE3P" aria-controls="popout_26157" aria-expanded="false" role="button" tabindex="0">Dank Memer</span>
                <span class="botTagCozy-3NTBvK botTag-1NoD0B botTagRegular-kpctgU botTag-7aX5WZ rem-3kT9wc">
                    <svg aria-label="Verified Bot" class="botTagVerified-2KCPMa" aria-hidden="false" width="16" height="16" viewBox="0 0 16 15.2"><path d="M7.4,11.17,4,8.62,5,7.26l2,1.53L10.64,4l1.36,1Z" fill="currentColor"></path></svg>
                    <span class="botText-1fD6Qk">BOT</span>
                </span>
            </span>
            <span class="timestamp-p1Df1m timestampInline-_lS3aK">
                <time aria-label="Today at 4:01 PM" id="message-timestamp-933149185031692388" datetime="2022-01-19T00:01:42.785Z"><i class="separator-AebOhG" aria-hidden="true"> — </i>Today at 4:01 PM</time>
            </span>
        </h2>
        <div id="message-content-933149185031692388" class="markup-eYLPri messageContent-2t3eCI">
            <strong>Work for Manager</strong> - Repeat Order - Remember words order!
            <code class="inline">quality</code>
            <code class="inline">manager</code>
            <code class="inline">resources</code>
            <code class="inline">revenue</code>
            <code class="inline">planning</code>
        </div>
    </div>
</div>

THEN

<div
    class="message-2CShn3 cozyMessage-1DWF9U mentioned-Tre-dv groupStart-3Mlgv1 wrapper-30-Nkg cozy-VmLDNB zalgo-26OfGz"
    role="article"
    data-list-item-id="chat-messages___chat-messages-933149185031692388"
    tabindex="-1"
    aria-setsize="-1"
    aria-roledescription="Message"
    aria-labelledby="message-username-933149185031692388 uid_1 message-content-933149185031692388 uid_2 message-timestamp-933149185031692388"
    aria-describedby=""
>
    <div class="contents-2MsGLg">
        <img src="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=128" aria-hidden="true" class="avatar-2e8lTP clickable-31pE3P" alt="d60c6bd5971f06776ba96497117f7f58" />
        <h2 class="header-2jRmjb" aria-describedby="reply-context-933149185031692388" aria-labelledby="message-username-933149185031692388 message-timestamp-933149185031692388">
            <span id="message-username-933149185031692388" class="headerText-2z4IhQ">
                <span class="username-h_Y3Us desaturateUserColors-1O-G89 clickable-31pE3P" aria-controls="popout_28275" aria-expanded="false" role="button" tabindex="0">Dank Memer</span>
                <span class="botTagCozy-3NTBvK botTag-1NoD0B botTagRegular-kpctgU botTag-7aX5WZ rem-3kT9wc">
                    <svg aria-label="Verified Bot" class="botTagVerified-2KCPMa" aria-hidden="false" width="16" height="16" viewbox="0 0 16 15.2">
                        <path d="M7.4,11.17,4,8.62,5,7.26l2,1.53L10.64,4l1.36,1Z" fill="currentColor"></path>
                    </svg>
                    <span class="botText-1fD6Qk">BOT</span>
                </span>
            </span>
            <span class="timestamp-p1Df1m timestampInline-_lS3aK">
                <time aria-label="Today at 4:01 PM" id="message-timestamp-933149185031692388" datetime="2022-01-19T00:01:42.785Z"><i class="separator-AebOhG" aria-hidden="true">—</i> Today at 4:01 PM</time>
            </span>
        </h2>
        <div id="message-content-933149185031692388" class="markup-eYLPri messageContent-2t3eCI">
            <span class="mention wrapper-1ZcZW- mention interactive" aria-controls="popout_28276" aria-expanded="false" tabindex="0" role="button">@Huskies</span> Click the buttons in correct order!
            <span class="timestamp-p1Df1m">
                <time aria-label="Edited Today at 4:01 PM" datetime="2022-01-19T00:01:55.053Z"><span class="edited-1v5nT8">(edited)</span></time>
            </span>
        </div>
    </div>
    <div id="message-accessories-933149185031692388" class="container-2sjPya">
        <div class="container-3Sqbyb">
            <div class="container-3nKPGI">
                <div class="children-2XdE_I">
                    <button type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                        <div class="contents-3ca1mk">
                            <div class="content-1xP6ZE" aria-hidden="false">
                                <div class="label-31sIdr">
                                    revenue
                                </div>
                            </div>
                        </div>
                    </button>
                    <button type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                        <div class="contents-3ca1mk">
                            <div class="content-1xP6ZE" aria-hidden="false">
                                <div class="label-31sIdr">
                                    planning
                                </div>
                            </div>
                        </div>
                    </button>
                    <button type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                        <div class="contents-3ca1mk">
                            <div class="content-1xP6ZE" aria-hidden="false">
                                <div class="label-31sIdr">
                                    resources
                                </div>
                            </div>
                        </div>
                    </button>
                    <button type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                        <div class="contents-3ca1mk">
                            <div class="content-1xP6ZE" aria-hidden="false">
                                <div class="label-31sIdr">
                                    quality
                                </div>
                            </div>
                        </div>
                    </button>
                    <button type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                        <div class="contents-3ca1mk">
                            <div class="content-1xP6ZE" aria-hidden="false">
                                <div class="label-31sIdr">
                                    manager
                                </div>
                            </div>
                        </div>
                    </button>
                </div>
            </div>
        </div>
    </div>
    <div class="buttonContainer-1502pf">
        <div class="buttons-3dF5Kd container-2gUZhU isHeader-2bbX-L" aria-label="Message Actions">
            <div class="wrapper-2vIMkT">
                <div class="button-3bklZh" aria-label="Add Reaction" aria-controls="popout_28330" aria-expanded="false" role="button" tabindex="0">
                    <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewbox="0 0 24 24">
                        <path
                            fill="currentColor"
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M12.2512 2.00309C12.1677 2.00104 12.084 2 12 2C6.477 2 2 6.477 2 12C2 17.522 6.477 22 12 22C17.523 22 22 17.522 22 12C22 11.916 21.999 11.8323 21.9969 11.7488C21.3586 11.9128 20.6895 12 20 12C15.5817 12 12 8.41828 12 4C12 3.31052 12.0872 2.6414 12.2512 2.00309ZM10 8C10 6.896 9.104 6 8 6C6.896 6 6 6.896 6 8C6 9.105 6.896 10 8 10C9.104 10 10 9.105 10 8ZM12 19C15.14 19 18 16.617 18 14V13H6V14C6 16.617 8.86 19 12 19Z"
                        ></path>
                        <path d="M21 3V0H19V3H16V5H19V8H21V5H24V3H21Z" fill="currentColor"></path>
                    </svg>
                </div>
                <div class="button-3bklZh" aria-label="Reply" role="button" tabindex="0">
                    <svg class="icon-1zidb7" width="24" height="24" viewbox="0 0 24 24">
                        <path d="M10 8.26667V4L3 11.4667L10 18.9333V14.56C15 14.56 18.5 16.2667 21 20C20 14.6667 17 9.33333 10 8.26667Z" fill="currentColor"></path>
                    </svg>
                </div>
                <div class="button-3bklZh" aria-label="Create Thread" role="button" tabindex="0">
                    <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewbox="0 0 24 24" fill="none">
                        <path
                            fill="currentColor"
                            d="M5.43309 21C5.35842 21 5.30189 20.9325 5.31494 20.859L5.99991 17H2.14274C2.06819 17 2.01168 16.9327 2.02453 16.8593L2.33253 15.0993C2.34258 15.0419 2.39244 15 2.45074 15H6.34991L7.40991 9H3.55274C3.47819 9 3.42168 8.93274 3.43453 8.85931L3.74253 7.09931C3.75258 7.04189 3.80244 7 3.86074 7H7.75991L8.45234 3.09903C8.46251 3.04174 8.51231 3 8.57049 3H10.3267C10.4014 3 10.4579 3.06746 10.4449 3.14097L9.75991 7H15.7599L16.4523 3.09903C16.4625 3.04174 16.5123 3 16.5705 3H18.3267C18.4014 3 18.4579 3.06746 18.4449 3.14097L17.7599 7H21.6171C21.6916 7 21.7481 7.06725 21.7353 7.14069L21.4273 8.90069C21.4172 8.95811 21.3674 9 21.3091 9H17.4099L17.0495 11.04H15.05L15.4104 9H9.41035L8.35035 15H10.5599V17H7.99991L7.30749 20.901C7.29732 20.9583 7.24752 21 7.18934 21H5.43309Z"
                        ></path>
                        <path
                            fill="currentColor"
                            d="M13.4399 12.96C12.9097 12.96 12.4799 13.3898 12.4799 13.92V20.2213C12.4799 20.7515 12.9097 21.1813 13.4399 21.1813H14.3999C14.5325 21.1813 14.6399 21.2887 14.6399 21.4213V23.4597C14.6399 23.6677 14.8865 23.7773 15.0408 23.6378L17.4858 21.4289C17.6622 21.2695 17.8916 21.1813 18.1294 21.1813H22.5599C23.0901 21.1813 23.5199 20.7515 23.5199 20.2213V13.92C23.5199 13.3898 23.0901 12.96 22.5599 12.96H13.4399Z"
                        ></path>
                    </svg>
                </div>
                <div class="button-3bklZh" aria-label="More" aria-controls="popout_28331" aria-expanded="false" role="button" tabindex="0">
                    <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewbox="0 0 24 24">
                        <path
                            fill="currentColor"
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M7 12.001C7 10.8964 6.10457 10.001 5 10.001C3.89543 10.001 3 10.8964 3 12.001C3 13.1055 3.89543 14.001 5 14.001C6.10457 14.001 7 13.1055 7 12.001ZM14 12.001C14 10.8964 13.1046 10.001 12 10.001C10.8954 10.001 10 10.8964 10 12.001C10 13.1055 10.8954 14.001 12 14.001C13.1046 14.001 14 13.1055 14 12.001ZM19 10.001C20.1046 10.001 21 10.8964 21 12.001C21 13.1055 20.1046 14.001 19 14.001C17.8954 14.001 17 13.1055 17 12.001C17 10.8964 17.8954 10.001 19 10.001Z"
                        ></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>
</div>

"""

"""
Soccer
<li id="chat-messages-933149790630449202" class="messageListItem-ZZ7v6g" aria-setsize="-1">
    <div
        class="message-2CShn3 cozyMessage-1DWF9U groupStart-3Mlgv1 wrapper-30-Nkg cozy-VmLDNB zalgo-26OfGz"
        role="article"
        data-list-item-id="chat-messages___chat-messages-933149790630449202"
        tabindex="-1"
        aria-setsize="-1"
        aria-roledescription="Message"
        aria-labelledby="message-username-933149790630449202 uid_1 message-content-933149790630449202 uid_2 message-timestamp-933149790630449202"
        aria-describedby=""
    >
        <div class="contents-2MsGLg">
            <img src="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=128" aria-hidden="true" class="avatar-2e8lTP clickable-31pE3P" alt=" " />
            <h2 class="header-2jRmjb" aria-describedby="reply-context-933149790630449202" aria-labelledby="message-username-933149790630449202 message-timestamp-933149790630449202">
                <span id="message-username-933149790630449202" class="headerText-2z4IhQ">
                    <span class="username-h_Y3Us desaturateUserColors-1O-G89 clickable-31pE3P" aria-controls="popout_8374" aria-expanded="false" role="button" tabindex="0">Dank Memer</span>
                    <span class="botTagCozy-3NTBvK botTag-1NoD0B botTagRegular-kpctgU botTag-7aX5WZ rem-3kT9wc">
                        <svg aria-label="Verified Bot" class="botTagVerified-2KCPMa" aria-hidden="false" width="16" height="16" viewBox="0 0 16 15.2">
                            <path d="M7.4,11.17,4,8.62,5,7.26l2,1.53L10.64,4l1.36,1Z" fill="currentColor"></path>
                        </svg>
                        <span class="botText-1fD6Qk">BOT</span>
                    </span>
                </span>
                <span class="timestamp-p1Df1m timestampInline-_lS3aK">
                    <time aria-label="Today at 4:04 PM" id="message-timestamp-933149790630449202" datetime="2022-01-19T00:04:07.171Z"><i class="separator-AebOhG" aria-hidden="true"> — </i>Today at 4:04 PM</time>
                </span>
            </h2>
            <div id="message-content-933149790630449202" class="markup-eYLPri messageContent-2t3eCI">
                <strong>Work for Professional Hunter</strong> - Soccer - Hit the ball!
                <span class="emojiContainer-2XKwXX" role="button" tabindex="0">
                    <img aria-label=":goal:" src="/assets/ff63bac8b064e04d31a32eeae8ccd7dc.svg" alt=":goal:" draggable="false" class="emoji" data-type="emoji" data-name=":goal:" />
                </span>
                <span class="emojiContainer-2XKwXX" role="button" tabindex="0">
                    <img aria-label=":goal:" src="/assets/ff63bac8b064e04d31a32eeae8ccd7dc.svg" alt=":goal:" draggable="false" class="emoji" data-type="emoji" data-name=":goal:" />
                </span>
                <span class="emojiContainer-2XKwXX" role="button" tabindex="0">
                    <img aria-label=":goal:" src="/assets/ff63bac8b064e04d31a32eeae8ccd7dc.svg" alt=":goal:" draggable="false" class="emoji" data-type="emoji" data-name=":goal:" />
                </span>
                [similar amounts of space as dragon and fish]
                <span class="emojiContainer-2XKwXX" role="button" tabindex="0">
                    <img aria-label=":levitate:" src="/assets/ab6a1028c6b247bcc472a4e9d0041228.svg" alt=":levitate:" draggable="false" class="emoji" data-type="emoji" data-name=":levitate:" />
                </span>

                <span class="emojiContainer-2XKwXX" role="button" tabindex="0"><img aria-label="⚽" src="/assets/376bdd3ac92afd53169e8faecf624110.svg" alt="⚽" draggable="false" class="emoji" data-type="emoji" data-name=":soccer:" /></span>
                <span class="timestamp-p1Df1m">
                    <time aria-label="Edited Today at 4:04 PM" datetime="2022-01-19T00:04:15.251Z"><span class="edited-1v5nT8">(edited)</span></time>
                </span>
            </div>
        </div>
        <div id="message-accessories-933149790630449202" class="container-2sjPya">
            <div class="container-3Sqbyb">
                <div class="container-3nKPGI">
                    <div class="children-2XdE_I">
                        <button role="button" type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                            <div class="contents-3ca1mk">
                                <div class="content-1xP6ZE" aria-hidden="false"><div class="label-31sIdr">Left</div></div>
                            </div>
                        </button>
                        <button role="button" type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                            <div class="contents-3ca1mk">
                                <div class="content-1xP6ZE" aria-hidden="false"><div class="label-31sIdr">Middle</div></div>
                            </div>
                        </button>
                        <button role="button" type="button" class="component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorGrey-2iAG-B sizeSmall-wU2dO- grow-2sR_-F">
                            <div class="contents-3ca1mk">
                                <div class="content-1xP6ZE" aria-hidden="false"><div class="label-31sIdr">Right</div></div>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="buttonContainer-1502pf">
            <div class="buttons-3dF5Kd container-2gUZhU isHeader-2bbX-L" aria-label="Message Actions">
                <div class="wrapper-2vIMkT">
                    <div class="button-3bklZh" aria-label="Add Reaction" aria-controls="popout_8388" aria-expanded="false" role="button" tabindex="0">
                        <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewBox="0 0 24 24">
                            <path
                                fill="currentColor"
                                fill-rule="evenodd"
                                clip-rule="evenodd"
                                d="M12.2512 2.00309C12.1677 2.00104 12.084 2 12 2C6.477 2 2 6.477 2 12C2 17.522 6.477 22 12 22C17.523 22 22 17.522 22 12C22 11.916 21.999 11.8323 21.9969 11.7488C21.3586 11.9128 20.6895 12 20 12C15.5817 12 12 8.41828 12 4C12 3.31052 12.0872 2.6414 12.2512 2.00309ZM10 8C10 6.896 9.104 6 8 6C6.896 6 6 6.896 6 8C6 9.105 6.896 10 8 10C9.104 10 10 9.105 10 8ZM12 19C15.14 19 18 16.617 18 14V13H6V14C6 16.617 8.86 19 12 19Z"
                            ></path>
                            <path d="M21 3V0H19V3H16V5H19V8H21V5H24V3H21Z" fill="currentColor"></path>
                        </svg>
                    </div>
                    <div class="button-3bklZh" aria-label="Reply" role="button" tabindex="0">
                        <svg class="icon-1zidb7" width="24" height="24" viewBox="0 0 24 24"><path d="M10 8.26667V4L3 11.4667L10 18.9333V14.56C15 14.56 18.5 16.2667 21 20C20 14.6667 17 9.33333 10 8.26667Z" fill="currentColor"></path></svg>
                    </div>
                    <div class="button-3bklZh" aria-label="Create Thread" role="button" tabindex="0">
                        <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path
                                fill="currentColor"
                                d="M5.43309 21C5.35842 21 5.30189 20.9325 5.31494 20.859L5.99991 17H2.14274C2.06819 17 2.01168 16.9327 2.02453 16.8593L2.33253 15.0993C2.34258 15.0419 2.39244 15 2.45074 15H6.34991L7.40991 9H3.55274C3.47819 9 3.42168 8.93274 3.43453 8.85931L3.74253 7.09931C3.75258 7.04189 3.80244 7 3.86074 7H7.75991L8.45234 3.09903C8.46251 3.04174 8.51231 3 8.57049 3H10.3267C10.4014 3 10.4579 3.06746 10.4449 3.14097L9.75991 7H15.7599L16.4523 3.09903C16.4625 3.04174 16.5123 3 16.5705 3H18.3267C18.4014 3 18.4579 3.06746 18.4449 3.14097L17.7599 7H21.6171C21.6916 7 21.7481 7.06725 21.7353 7.14069L21.4273 8.90069C21.4172 8.95811 21.3674 9 21.3091 9H17.4099L17.0495 11.04H15.05L15.4104 9H9.41035L8.35035 15H10.5599V17H7.99991L7.30749 20.901C7.29732 20.9583 7.24752 21 7.18934 21H5.43309Z"
                            ></path>
                            <path
                                fill="currentColor"
                                d="M13.4399 12.96C12.9097 12.96 12.4799 13.3898 12.4799 13.92V20.2213C12.4799 20.7515 12.9097 21.1813 13.4399 21.1813H14.3999C14.5325 21.1813 14.6399 21.2887 14.6399 21.4213V23.4597C14.6399 23.6677 14.8865 23.7773 15.0408 23.6378L17.4858 21.4289C17.6622 21.2695 17.8916 21.1813 18.1294 21.1813H22.5599C23.0901 21.1813 23.5199 20.7515 23.5199 20.2213V13.92C23.5199 13.3898 23.0901 12.96 22.5599 12.96H13.4399Z"
                            ></path>
                        </svg>
                    </div>
                    <div class="button-3bklZh" aria-label="More" aria-controls="popout_8389" aria-expanded="false" role="button" tabindex="0">
                        <svg class="icon-1zidb7" aria-hidden="false" width="24" height="24" viewBox="0 0 24 24">
                            <path
                                fill="currentColor"
                                fill-rule="evenodd"
                                clip-rule="evenodd"
                                d="M7 12.001C7 10.8964 6.10457 10.001 5 10.001C3.89543 10.001 3 10.8964 3 12.001C3 13.1055 3.89543 14.001 5 14.001C6.10457 14.001 7 13.1055 7 12.001ZM14 12.001C14 10.8964 13.1046 10.001 12 10.001C10.8954 10.001 10 10.8964 10 12.001C10 13.1055 10.8954 14.001 12 14.001C13.1046 14.001 14 13.1055 14 12.001ZM19 10.001C20.1046 10.001 21 10.8964 21 12.001C21 13.1055 20.1046 14.001 19 14.001C17.8954 14.001 17 13.1055 17 12.001C17 10.8964 17.8954 10.001 19 10.001Z"
                            ></path>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </div>
</li>
"""

"""
MATCH COLOR BEFORE:
<div id="message-content-939604327402709044" class="markup-eYLPri messageContent-2t3eCI">
  <strong>Work for Developer</strong>- Color Match - Match the color to the selected word.
  <span class="emojiContainer-2XKwXX" role="button" tabindex="0"><img aria-label=":Black:" src="https://cdn.discordapp.com/emojis/863886248431190066.webp?size=80&amp;quality=lossless" alt=":Black:" draggable="false" class="emoji" data-type="emoji" data-id="863886248431190066"></span>
  <code class="inline">hacker</code>
  <span class="emojiContainer-2XKwXX" role="button" tabindex="0"><img aria-label=":Yellow:" src="https://cdn.discordapp.com/emojis/863886248296316940.webp?size=80&amp;quality=lossless" alt=":Yellow:" draggable="false" class="emoji" data-type="emoji" data-id="863886248296316940"></span>
  <code class="inline">object</code>
  <span class="emojiContainer-2XKwXX" role="button" tabindex="0"><img aria-label=":Marine:" src="https://cdn.discordapp.com/emojis/863886248572878939.webp?size=80&amp;quality=lossless" alt=":Marine:" draggable="false" class="emoji" data-type="emoji" data-id="863886248572878939"></span>
  <code class="inline">development</code>
</div>
MATCH COLOR AFTER:

"""

"""
MEMORIZE EMOJI BEFORE:
<div id="message-content-939619617981202503" class="markup-eYLPri messageContent-2t3eCI"><strong>Work for Santa Claus</strong> - Emoji Match - Look at the emoji closely!
    <span class="emojiContainer-2XKwXX" role="button" tabindex="0">
        <img aria-label="😌" src="/assets/817f965bd1fd796777908e6c8052d665.svg" alt="😌" draggable="false" class="emoji" data-type="emoji" data-name=":relieved:">
    </span>
</div>

AFTER:

"""