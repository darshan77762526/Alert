import json
import requests
import time

# ==========================================
# ⚙️ SECURE HARDCODED LIVE CONFIGURATION
# ==========================================
TELEGRAM_TOKEN = "8830701721:AAFKEoD9elwvYrr9no7O8TvsAmGWh4krfyY"
TELEGRAM_CHAT_ID = "-1004296644580"

# Using triple quotes ensures your long mobile cookie data string never causes a SyntaxError
SHEIN_COOKIE_STRING = """_abck=B6388F6AD33867C23568F81952EBDBF0~0~YAAQNWfRF3BH2F2eAQAA0+TMbQ+Gh2mMl2dTOPtBmbhZ0+ptByb9F281m7rsWuPRhxc+TznqsD8yMdECIrz/uDopdML45SnZLs7xgBE+vz7Jin9XyFzOV8vRtf2JaAzoU5fF5YmNtFhbbyR5hZm/iTowQK8w2bIK3QvOcc3AU8nomUCrH7IzKpAenj5MgNrVQT6irc/xR+bWayUP5Ap26tqMkkHD5FOQXosXK+ih5H/EWy/srIil1uCL5jqYS3li6Pf5HI2j7zjCfwuzdpcmOZqqwGO7r+SO4CcUCtXxp36XJeOPPFXdHiKxemvaeXye9K9V+fesIuw2tBvPkpoXxVSmxRvyS/nuksUlayeOoeRgq9YO47ScRrG4O6G7+DhtLQynQQaW09AGO1Tr+uHp6Cwzvcn7UHLuIee++E8cpycy4oAVXNPmL5x9en+1Fg6ahUzD0Qo3bWAyvG6gucpYlibSuGPk6C5MlaDcO69wMcwI3Js5a68p1YSL45c+Uoeg0SIWE+nAhF1LStdd6x92RcBGRA2dxmJK/pl9P0OSNpNchyLHSa/Bo1JElKbgZKWHSAFZeLznPad5tOvTOVH0Y3CkISemlS4JWcRkBiLpSQ/er/KOGtsM+V+vYkpq/7trV6V0d3b/jcC1ZBs4xUYGYwOgIH1F+ju55JqQJavgK+wTjxyuuhO0ubx29EdT3mW7woDqOQkYeMO0vubBJ1NjvB69ogXLxcnEDJNS1lmNhhIzbZUyLhbUONrik8oBruEXpk1qnhBGtiFdGS/kkW99T6w4KF4n1ckAcBuDf9siQ6wX9srjHWydvSf93xYXDfAUMcOEiQR7oFnNyZuKc41LOx5hDKy4tyD7Pd1gzMqoQyYZiGY8VEx109Nn50k6jM0TfshHsBc+SPhmqnWyo4WQqT7B~-1~-1~1779960992~AAQAAAAF%2f%2f%2f%2f%2f0WUp8mcPgzXH8snjgyg4iwJJ3iCW6lV05zneAw0OIfTvgCmNSa4c9PGKJ+u9NhxU48RMXyBS9cw61sw5lK%2f4C0nHR9MRo2khMO1~-1;_gcl_aw=GCL.1779957327.EAIaIQobChMI1eP82cnblAMVySfUAR0x2Sg3EAAYASAAEgLMVfD_BwE;SN=Darshan;bm_sz=D5875524B706C47E48E696B7B647F1E9~YAAQNWfRF3NH2F2eAQAA0+TMbR/Etb061eq6B1e01OlziM2wrjgnDm+gzYjiHLt/0yXzE0BwhMnlropPgOthBWOpNyIalIXl58M6jPJo489kCUJHzhmZdCi/+CTcnFuyQOcepYIyQW7/syzXrA2TOCdM7nqNsztfdzDAk/mgPEiICJolvNCO4nS4GAM+suBZxJ265kKa+Jikik3qD3IZl+Lm4vIFQYJXFOvaw+DGU0UXM07afAjJcWm+/OO8BVN4CMkkDBT7CyECv/XCBvnosL5tMOX9niRvPRgbzfZLhHUu3JB94oUdT1lhJ200cMhCuHE2fmGhpV8XUjwGeypGXZFzw3uoFeZeX+7+yOFGu2v7jqPoEzxk/sDF+Fd35SjX+TaRL8t2RIeT9NxinbpKuE7hHvWzKNH5gKawB3NL+OH7w/UN4Zd/zTI/Bha+kqj5T1rheNqKVCnUYmuD0UPqQO3+hgqsaqwLAy6+jAAg8M/qic5FkjMm3wzWfAza7BskoERyAJ4yNB9Y55NUK4pL0znOBohCtgb6vPa6~3747888~3424569;CT=NAGPUR;_ga_F1NJ1E2HJ2=GS2.1.s1779957328$o1$g1$t1779958606$j60$l0$h0;ak_bmsc=9CDB49C9DACDFB5A74A766EEFB2D3E2C~000000000000000000000000000000~YAAQN2fRF2+60l6eAQAAqzy5bR8X/WVlM8ajA15qE4Bwh7Ig/hqlgcL+6EBcWgwtkEuB3rTXicmwT5dnTkVjBDn4xN92NuGN7hrAQvvGSb5SyGiOKM0N3slAT2E196ENzQ1qSU3HzZpgFDNMWAtoX1iFJ0qO/j/2a6IncdPElFJyv/Q6QipdC1/Ud8G/9gTDkAKOGha5L/+tYt90QXbKeeCrlnvoorCxF7M0k/kUb3+eAwET4Z2vHGwpysNhTK7hdzui8y1GhR+TTKXASn/4FyCsCOEVDg/wp28aQbNBYbF1tE/CxrYGIQxAnPv9vevMh0e0uTKF3g1+CYJH8if8FpHaBEDtmGjro9aUasyhjkSjXrKnDPMgr+wVe/oHpKG0Ly4WJYMnV5TRJxwQixCBz3W6WNcpMfdhfdkJJdrfUja0zUoiu5UNLzdr67E/BSORSnKfBcqV3nzRwE9rSIsI9Lm2qaENk5NuI/45/qwJWZ0=;_gat=1;ST=MAHARASHTRA;WZRK_S_8WR-85Z-WR7Z=%7B%22p%22%3A15%2C%22s%22%3A1779957316%2C%22t%22%3A1779958610%7D;bm_so=78E9D186E614E97BD075E470EA716F2CC0CB35B16AE1D68942CBD6FF5289570D~YAAQNWfRF61F2F2eAQAAqcTMbQd491zrFQJuAI+LsBVccFI3qdeP399FVnDuy785wQj2q9qH4TVBxTrOiJoaAUVdyPsxQHpaCBuP8fa6+6SxCEznKoC5eannauxZMDJodzgWMU2QTknkNH3z2/ELY86j+bon6Du/1UWuiTPFEGrca3JvLG7A+rg0t92tBUfhwadKBdI6ZtSpQfYe2D81fWk2Bnn56xEWG4YpivmeNw+AHcoFIBZwi4nvuRhMGZOutlNed2aM45ilW2S74AReUwcOVJNbykMCQ+0oKd7D/vmjCYMaIUb2Yhh9p8xxJXZ1ZQu7cm6vj3ufDhda4dGiMmubYQQmbCeZJZvuxmZNcvqZGkQ3YEHvvDMRO9jxJ3h/8xlktLpo7fr8xI5hi+Ej+W1pkj0L76NBGMt0+jbVWNFPl9jj/jNxo/M4pt8/d1/oAEbk3pJH9AIQMRbuqkLIBpsptlgkKA7wLb+YbNCuHtAhI61fQPS6iXZCFbEh+Q==;CI=6e0818f8-f38e-4a8c-be46-ac6c33198ae7;bm_s=YAAQNWfRF9FH2F2eAQAAaOzMbQV7Jl7gOunU2P3c+2kZ8II2G5qoniHHQzVPC6XycFvoelAn4d6icvMjnM+AruaQmXas+a//gNPzUoq2wgb642XACY5a8J4RB/233at28zs7/r3uy1qNEmCxFGQ9FO6y0exaR1xKhbAdrgWQx+fXsW9vQpjs3/zm4U4ZG7kx1BJp3b7idbi3kwSOxpczZzhlJJ3ud+3iHHH8CYQepIkFdQw0tbkftOsRdOlKOchjhABTqyfOFh+d+0/ZEn4B9oo873Cc987rrzN7RMlC3f/pbxiyRINi6fEdJZ05Fu9MVXIQ4Mdtdo2kiwv428r1UmB2aJQuyoGpr3aJGmkMp7IcvHvlkXRDm/g8nAjQhqPqGXpvfZuhoy+JEa37gNHQIHIE9cB/r9KnakQtTKPuWVmyuwTjiRDIytkX+cE7qk/VLEqgk6QwAKUx9/Mt38LAcyWLU6/mbeNDxUXFih2kpfg8fS3X4NSt5udTnELG9Bi16xkWlN8nTmQLowgMoEmOSYFEw+A4dzhdmC7d0Q6p3mttOdxxCvajbOutXJB3ZRWFC79AY/281F/Vxs6353HQF0uvN+JJTr/gDH+HmVXr4vM1Ks6H7KXCmgf/vgVBkJCqszH2UwXPKZuyLfKUJMBWY5j19BageyeLWZ/wA3zQ5cHaJKde+Ub6AHCdwgjW1D6KfEf1InysMvC/gXsaIXvfoWVHzC1CudLL/jlywZc5gk14f9IjtiyAQMIiSPIiNJA0fr5dXiQDJAtiPoAs0o1K+ZZUdFGEqevC84VBWCOs0T/pK8kg7J4klmUNcMbX83J2o0v0GK+8LZGSkdMxgn3af8NbdCFtOYN7wF2TC4dna1wV3LIIHh5tZzfcArnuvE9O6jomNYr2Xf7/RXRGeqOoWiZ8KsO+rpasq2WyeZQ7rDWBRnfndzTs5Lo6JhKuS7qpYGaaiLEFrQ5CXU+A==;ZN=undefined;customerType=Existing;un=Darshan%20;uI=iiscbanglore2804%40gmail.com;_ga=GA1.1.1807697703.1779957317;_fbp=fb.1.1779957318730.18127083088160942;R=eyJhbGciOiJSUzI1NiJ9.eyJzZXNzaW9uIjp7InNlc3Npb25JZCI6ImZiZTYyNzVhLWQyNWUtNGJlOC05ODQ3LTAwN2RhYzkxYjc0ZSIsImNsaWVudE5hbWUiOiJ3ZWJfY2xpZW50Iiwicm9sZXMiOlt7Im5hbWUiOiJST0xFX0NVU1RPTUVSR1JPVVAifV19LCJ0eXBlIjoicmVmcmVzaCIsInRlbmFudElkIjoiU0hFSU4iLCJzdWIiOiJzaGVpbl9paXNjYmFuZ2xvcmUyODA0QGdtYWlsLmNvbSIsImV4cCI6MTc5NTUwOTM1OCwiaWF0IjoxNzc5OTU3MzU4fQ.j4pRPTRpmJGhcCB1mO7d4Nys97mnxfC_LWQzvsvwOshpieuluf89c5QB3K4I3nVsE6otXtZnpg33V3V738gkidg0yQOslmOP6I-bYLyYK12MxT0qcZkcsatIZBDKjMJpgMQcAeJcOBGVHpOgbHOEfRAV12btNuJPPqAuWsgZXylgaIOcLwq038fKSt2gTgaf4xTYSwENMFWyEb9Us-99IK8EA0Ihzu9Sj3SdQVUEI-IgxnDti3MFlBAcurD61bjaf-U_VVfyPpOcv-yhnqX1XyCPnR1PdiPxD2NAW5hN4sSWAGEN4rr2miUi5ZA74B8zmrFesRGSX1FnYY22y9np5w;_gcl_au=1.1.864405076.1779957318;A=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzaGVpbl9paXNjYmFuZ2xvcmUyODA0QGdtYWlsLmNvbSIsInBrSWQiOiI2ZTA4MThmOC1mMzhlLTRhOGMtYmU0Ni1hYzZjMzMxOThhZTciLCJjbGllbnROYW1lIjoid2ViX2NsaWVudCIsInJvbGVzIjpbeyJuYW1lIjoiUk9MRV9DVVNUT01FUkdST1VQIn1dLCJtb2JpbGUiOiI4ODg4MjE3MzAzIiwidGVuYW50SWQiOiJTSEVJTiIsImV4cCI6MTc5NTUwOTM1OCwidXVpZCI6IjZlMDgxOGY4LWYzOGUtNGE4Yy1iZTQ2LWFjNmMzMzE5OGFlNyIsImlhdCI6MTc3OTk1NzM1OCwiZW1haWwiOiJpaXNjYmFuZ2xvcmUyODA0QGdtYWlsLmNvbSJ9.U0ZysNvZN8RFm4uRomZsNuKl9tyjTQ0rirQ7_8cdVXCzKVmYxp0AmKiGG0iMVqo8IUOvl_lBWqe2PVHc4AqIEN0UanJd1OXgp6Y0WqPhzwtWSanb7XXlwhGmU4E7OMfluC_Rwu-BAx9QIeWq62wIjoGgji42ZSixhmI1FdqiIl6K4DRrjIjyTbzpuCZu-b4Y1-a2q-fz82-UytPv-iwBml3RTd2RDvXpQT3zQ1lvTbM0OvJmSgMnoZurZslCnIFZOPjNZFzMyAl1EMKfarqt94KaYZNEea57oDbtM-1FWGqrb8AMlrDLVcPMt3GMjgBJFxG3l0ax0Ruh4a8reRiw6Q;PK=vPkxcraIVa1SYB8b5k6gxuULmfIZCw22iFcW7kHOVZiehdZiIRIPXChQh32NzvWy;U=iiscbanglore2804%40gmail.com;_gac_G-D6SVDYBNVW=1.1779957317.EAIaIQobChMI1eP82cnblAMVySfUAR0x2Sg3EAAYASAAEgLMVfD_BwE;jioAdsFeatureVariant=true;deviceId=dQk74aEcziz6USy5zDpdS;G=M;bm_lso=78E9D186E614E97BD075E470EA716F2CC0CB35B16AE1D68942CBD6FF5289570D~YAAQNWfRF61F2F2eAQAAqcTMbQd491zrFQJuAI+LsBVccFI3qdeP399FVnDuy785wQj2q9qH4TVBxTrOiJoaAUVdyPsxQHpaCBuP8fa6+6SxCEznKoC5eannauxZMDJodzgWMU2QTknkNH3z2/ELY86j+bon6Du/1UWuiTPFEGrca3JvLG7A+rg0t92tBUfhwadKBdI6ZtSpQfYe2D81fWk2Bnn56xEWG4YivmeNw+AHcoFIBZwi4nvuRhMGZOutlNed2aM45ilW2S74AReUwcOVJNbykMCQ+0oKd7D/vmjCYMaIUb2Yhh9p8xxJXZ1ZQu7cm6vj3ufDhda4dGiMmubYQQmbCeZJZvuxmZNcvqZGkQ3YEHvvDMRO9jxJ3h/8xlktLpo7fr8xI5hi+Ej+W1pkj0L76NBGMt0+jbVWNFPl9jj/jNxo/M4pt8/d1/oAEbk3pJH9AIQMRbuqkLIBpsptlgkKA7wLb+YbNCuHtAhI61fQPS6iXZCFbEh+Q==~1779958599774;_fpuuid=dQk74aEcziz6USy5zDpdS;_ga_D6SVDYBNVW=GS2.1.s1779957318$o1$g1$t1779958614$j46$l0$h1258443293;_gcl_gs=2.1.k1$i1779957315$u63390829;_gid=GA1.2.2057723687.1779957317;bm_ss=ab8e18ef4e;bm_sv=6FEA0300A9E05A3111D9B69F85B943F4~YAAQNWfRFzhI2F2eAQAAa/bMbR9cwObrwlCfKTBGFFI12Et6VkpDwgw5guD1/hk2msbuafkLkw3HTCM+8ys6T4ZQ9Y5HRhEauwQiBEVYmh/gkvIjM4Qr1BvrFYvePQB1RudP17aZdeSzSU/sud5GqNi4OMAfsF5LsJ9tv5Xr0w2Tsb+DL3fqlF5aQA2ozTBEIvptmJcS05r+/1nIn5KS/XfL7hrtnkPAS6zx3urhNqOoykmBNh55JJdLcNV3y3XSmmLX0w==~1;customerType=Existing;deviceCohortValue=%5B%5D;EI=kL2pVCaEYfKFU0SVCc0LcCHY7MTcyzFH5ySW7mhmo6V9iQHQoDF69KFLakmjcLIZ;ifa=a2b6bd06-e34e-43a5-b419-887adb91f749;LS=LOGGED_IN;mE=she*******************%40gmail.com;mN=88XXXXX303;MN=8888217303;navigation_cookie=false;os=3;perf=true;PG=;sessionId=sess_1779958596419_rlw2d8jfg;TS0119eff6=015d0fa2265700e65662bf4c4b8a234484ecf02f611e5906fb8e6e19c250e089bbc9f3494aefea098faf53374e7c8632cce1cf4aae;TS01b6f9b7=015d0fa2265700e65662bf4c4b8a234484ecf02f611e5906fb8e6e19c250e089bbc9f3494aefea098faf53374e7c8632cce1cf4aae;userCohortValues=[{"key":"shein_v1","value":"economy|na,noreturn_pilot,na,women,cl30d"}];V=1;vr=WEB-2.0.11;WZRK_G=faf345270c2f4a37bd7132ad1f14ae69"""

# Load or generate sent tracking file list to avoid duplication loops
SENT_ITEMS_FILE = "sent_items.json"
try:
    with open(SENT_ITEMS_FILE, "r") as f:
        SENT_ITEMS = set(json.load(f))
except Exception:
    SENT_ITEMS = set()

def send_telegram_alert(item_title, item_price, item_link):
    message = (
        f"🚨 **NEW SHEIN STOCK DETECTED** 🚨\n\n"
        f"👕 **Item:** {item_title}\n"
        f"💰 **Price:** {item_price}\n"
        f"🔗 **Link:** [Click to Open Item]({item_link})"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Failed alert delivery matrix: {e}")

def scan_shein_secure_api(keyword, size_filter):
    print(f"Scanning data pipelines for: {keyword} ({size_filter})...")
    api_url = "https://www.shein.com/api/search/v1/products"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Cookie": SHEIN_COOKIE_STRING.strip(),
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.shein.com/"
    }
    
    params = {
        "keyword": keyword,
        "limit": "30",
        "sort": "7",              # Price: Low to High
        "price_max": "250",       # Your specific budget cap
        "size_filter": size_filter
    }
    
    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            products = data.get("info", {}).get("products", [])
            
            for product in products:
                title = product.get("title", "")
                price = product.get("price", {}).get("retailPrice", {}).get("amount", "250")
                currency = product.get("price", {}).get("retailPrice", {}).get("symbol", "₹")
                display_price = f"{currency}{price}"
                
                relative_url = product.get("url", "")
                full_url = f"https://www.shein.com{relative_url}"
                product_id = str(product.get("id", ""))
                
                if product_id not in SENT_ITEMS:
                    SENT_ITEMS.add(product_id)
                    send_telegram_alert(title, display_price, full_url)
        else:
            print(f"Pipeline verification status rejection code: {response.status_code}")
    except Exception as e:
        print(f"Scanning anomaly caught: {e}")

if __name__ == "__main__":
    scan_shein_secure_api("men t-shirt", "S")
    time.sleep(3)
    scan_shein_secure_api("men pants", "30")
    
    with open(SENT_ITEMS_FILE, "w") as f:
        json.dump(list(SENT_ITEMS), f)
    
