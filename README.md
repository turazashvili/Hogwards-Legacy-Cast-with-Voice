# ⚡ Hogwarts Spell Caster

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![AssemblyAI](https://img.shields.io/badge/AssemblyAI-Universal--Streaming-purple.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A **real-time voice-controlled spell casting system** that transforms spoken Harry Potter spells into instant keyboard commands using AssemblyAI's Ultra-Fast Universal-Streaming technology. Cast spells with your voice and watch them trigger game actions in under 300ms!

## 🎯 Features

- ⚡ **Ultra-Low Latency**: Sub-300ms response time from speech to action
- 🎭 **30+ Harry Potter Spells**: Complete spell repertoire from the wizarding world
- 🧠 **Intelligent Recognition**: Advanced fuzzy matching handles pronunciation variations
- 🚀 **Partial Processing**: Acts on incomplete words for instant response
- 🛡️ **Spam Prevention**: Smart cooldowns prevent accidental rapid-fire casting
- 🎮 **Gaming Ready**: Direct keyboard integration for seamless game control
- 🔧 **Optimized Performance**: Pre-computed variations and early-exit logic

## 🎬 Demo

[Hogwarts Spell Caster Demo](https://youtu.be/RRjN_gkcMDg?si=0LejjrSE1rSjr_xe)

*Click to watch the magic in action!*

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Microphone access
- AssemblyAI API key (free tier includes $50 credits)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/turazashvili/Hogwards-Legacy-Cast-with-Voice
   cd Hogwards-Legacy-Cast-with-Voice
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv hogwarts
   
   # Windows
   hogwarts\Scripts\activate
   
   # macOS/Linux
   source hogwarts/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get AssemblyAI API Key**
   - Sign up at [AssemblyAI](https://www.assemblyai.com/)
   - Get your free API key from the dashboard
   - Copy the key for the next step

 5. **Set up environment variables**
    
    **Option A: Using .env file (Recommended)**
    ```bash
    # Copy the example environment file
    cp .env.example .env
    
    # Edit .env and replace 'your_api_key_here' with your actual AssemblyAI API key
    # Then load it before running:
    
    # Windows (PowerShell)
    Get-Content .env | ForEach-Object { if($_ -match '^([^=]+)=(.*)$'){ [Environment]::SetEnvironmentVariable($matches[1], $matches[2]) } }
    
    # macOS/Linux (bash/zsh)
    export $(cat .env | xargs)
    ```
    
    **Option B: Set directly**
    ```bash
    # Windows (Command Prompt)
    set ASSEMBLYAI_API_KEY=your_api_key_here
    
    # Windows (PowerShell)
    $env:ASSEMBLYAI_API_KEY="your_api_key_here"
    
    # macOS/Linux
    export ASSEMBLYAI_API_KEY=your_api_key_here
    ```

6. **Run the spell caster**
   ```bash
   python spell_caster.py
   ```

## 🪄 Usage

### Basic Operation

1. **Start the application**
   ```bash
   python spell_caster.py
   ```

2. **Wait for the listening prompt**
   ```
   🎤 Listening for spells...
   ```

3. **Speak a spell clearly**
   - "Lumos" → Presses F1+1
   - "Wingardium Leviosa" → Presses F1+2
   - "Stupefy" → Presses F2+1

4. **Watch the magic happen!**
   ```
   ⚡ Casting lumos - f1+1
   ```

### Tips for Best Results

- 🗣️ **Speak clearly** and at normal volume
- ⏱️ **Pause briefly** after each spell (0.5s minimum)
- 🎯 **Use exact spell names** or close variations
- 🔇 **Minimize background noise** for better accuracy
- 🎮 **Have your game/application focused** to receive keyboard commands

## 🧙‍♂️ Complete Spell List

### Basic Spells (F1 + Number)
| Spell | Variations | Keyboard Command | Description |
|-------|------------|------------------|-------------|
| `lumos` | - | `F1+1` | Light spell |
| `levitate` | `levi os o`, `levioso`, `wingardium leviosa` | `F1+2` | Levitation spell |
| `incendio` | `disarm` | `F1+3` | Fire/disarm spell |
| `summon` | `axio`, `exhale` | `F1+4` | Summoning spell |

### Combat Spells (F2 + Number)
| Spell | Variations | Keyboard Command | Description |
|-------|------------|------------------|-------------|
| `stun` | `stupefy` | `F2+1` | Stunning spell |
| `ward` | - | `F2+2` | Protection spell |
| `repair` | `reparo` | `F2+3` | Repair spell |
| `bind` | `petrificus` | `F2+4` | Binding spell |

### Advanced Spells (F3 + Number)
| Spell | Variations | Keyboard Command | Description |
|-------|------------|------------------|-------------|
| `ignite` | - | `F3+1` | Ignition spell |
| `freeze` | `glacius` | `F3+2` | Freezing spell |
| `arrest` | `momentum` | `F3+3` | Movement control |
| `blast` | `confringo` | `F3+4` | Explosive spell |

### Master Spells (F4 + Number)
| Spell | Variations | Keyboard Command | Description |
|-------|------------|------------------|-------------|
| `banish` | `depulso` | `F4+1` | Banishing spell |
| `shatter` | `reducto` | `F4+2` | Destructive spell |
| `patronum` | - | `F4+3` | Patronus charm |
| `mend` | - | `F4+4` | Mending spell |

### Utility Spells
| Spell | Keyboard Command | Description |
|-------|------------------|-------------|
| `protego` | `Q` | Shield charm |
| `revelio` | `R` | Revealing charm |

## ⚙️ Configuration

### Custom Spell Mapping

Edit the `SPELLS` dictionary in `spell_caster.py` to add or modify spells:

```python
SPELLS = {
    "your_spell": "key_combination",
    "expelliarmus": "f1+3",  # Custom mapping
    "avada kedavra": "ctrl+alt+delete",  # Dangerous spell!
}
```

### Performance Tuning

Adjust streaming parameters for your needs:

```python
StreamingParameters(
    sample_rate=16000,
    format_turns=True,
    end_of_turn_confidence_threshold=0.5,  # Lower = faster response
    min_end_of_turn_silence_when_confident=100,  # Minimum silence (ms)
    max_turn_silence=1500,  # Maximum silence before timeout
)
```

### Recognition Sensitivity

Modify confidence thresholds:

```python
# In process_transcript function
confidence_threshold=0.6,  # Lower = more sensitive
actual_threshold = confidence_threshold + 0.2 if is_partial else confidence_threshold
```

## 🔧 Technical Architecture

### Core Components

1. **AssemblyAI Universal-Streaming**: Real-time speech-to-text with 300ms latency
2. **Optimized Fuzzy Matching**: Multi-layer spell recognition system
3. **Partial Transcript Processing**: Immediate response to incomplete speech
4. **Spam Prevention**: Time-based cooldowns and duplicate detection
5. **Keyboard Integration**: Direct system command execution

### Performance Optimizations

- **Pre-computed Variations**: Spell variations cached for O(1) lookup
- **Early Exit Logic**: Avoids expensive operations when exact matches found
- **Dual-Layer Processing**: Handles both partial and complete transcripts
- **Intelligent Thresholding**: Dynamic confidence adjustment for speed vs accuracy

### Flow Diagram

```
Speech Input → AssemblyAI → Transcript → Fuzzy Matching → Spell Found → Keyboard Command → Game Action
     ↓              ↓           ↓            ↓             ↓              ↓              ↓
   Audio         300ms      Partial/     Pre-computed   Command       Key Press     Instant
  Stream         Latency    Complete     Variations     Mapping       Execution     Response
```

## 🎮 Gaming Integration

### Supported Games

This spell caster works with any game or application that accepts keyboard input:

- **Hogwarts Legacy** ⭐ (Perfect match!)
- **Skyrim** with magic mods
- **World of Warcraft** 
- **Any game with customizable keybinds**

### Setup for Games

1. **Configure game keybindings** to match spell commands (F1+1, F1+2, etc.)
2. **Run the spell caster** before starting your game
3. **Alt-tab** to the game window 
4. **Start casting spells** with your voice!

### Example Hogwarts Legacy Setup

```
F1+1 → Basic Cast
F1+2 → Levioso
F1+3 → Incendio
F2+1 → Stupefy
Q → Protego
R → Revelio
```

## 🚨 Troubleshooting

### Common Issues

**🔇 "No microphone detected"**
- Check microphone permissions
- Ensure microphone is set as default recording device
- Try running as administrator (Windows)

**🤖 "Poor spell recognition"**
- Reduce background noise
- Speak closer to microphone
- Lower confidence threshold in configuration
- Check API key is set correctly

**⌨️ "Keyboard commands not working"**
- Ensure target application has focus
- Check if game/app accepts the key combinations
- Try running as administrator for system access
- Verify keyboard library compatibility

**⚡ "High latency/slow response"**
- Check internet connection (streaming requires bandwidth)
- Reduce `min_end_of_turn_silence_when_confident` value
- Lower `end_of_turn_confidence_threshold`
- Close other bandwidth-intensive applications

### Debug Mode

Enable detailed logging by modifying the logging level:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Spells

1. Fork the repository
2. Add spells to the `SPELLS` dictionary
3. Update the README spell list
4. Test pronunciation variations
5. Submit a pull request

### Performance Improvements

- Optimize fuzzy matching algorithms
- Improve spell variation detection
- Enhance partial transcript processing
- Add pronunciation learning

### Feature Requests

- Multi-language support
- Custom voice commands
- Visual feedback system
- Mobile app integration

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **AssemblyAI** for the incredible Universal-Streaming technology
- **J.K. Rowling** for creating the magical world of Harry Potter
- **The Python Community** for amazing libraries and tools
- **Voice AI Developers** pushing the boundaries of real-time processing

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=turazashvili/Hogwards-Legacy-Cast-with-Voice&type=Date)](https://star-history.com/#turazashvili/Hogwards-Legacy-Cast-with-Voice&Date)

---

**Made with ⚡ by [turazashvili](https://github.com/turazashvili)**

*"It's LeviOsa, not LeviosA!" - Hermione Granger*

🔗 **Links**: [Demo Video](https://youtu.be/RRjN_gkcMDg?si=0LejjrSE1rSjr_xe) | [GitHub Repository](https://github.com/turazashvili/Hogwards-Legacy-Cast-with-Voice) | [AssemblyAI Challenge](https://dev.to/challenges/assemblyai-2025-07-16) 