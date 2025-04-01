- For database, use autotitle/db.

    ```shell
     db
    └──  series-name          # ID of series
        ├──  fillers.txt      # Fillers list `,` separated
        └──  names.txt        # Names of the episode. format: "episode num" "episode name", one ep at one line
    ```

- For user config, it will be dir specific. It will contain `_autotitle.jsoc`:

  ```json
  {
    "series": [
      "detective-conan" //id of the anime thiis dir contains. fillers, ep titles will be added for this series
    ],
    "pattern": {
      "episodes": {
        "input": [
          "Detective Conan Remastered - {{EP_NUM}} {{RES}}.{{EXT}}", // Input: "Detective Conan Remastered - 123 1080p.mkv"
          "ep {{EP_NUM}} {{TITLE}}.{{EXT}}"                          // Input: "ep 123 - The Weather Girl Case.mkv"
        ],
        "output": [
          "DC {{EP_NUM}} {{FILLER}} - {{TITLE}} - {{RES}}.{{EXT}}"   // Output: "DC 123 [F] - The Weather Girl Case - 1080p.mkv"
        ]
      },
      "movies": {
        "input": [
          "Detective Conan Remastered - Movie {{MV_NUM}} {{RES}}.{{EXT}}" // Input: "Detective Conan Movie 1 1080p.mkv"
        ],
        "output": [
          "DC Movie {{MV_NUM}} - {{TITLE}} - {{RES}}.{{EXT}}"            // Output: "DC Movie 1 - The time bomber - 1080p.mkv"
        ]
      }
    },
    "formats": [ // extensions to check for. will be apended with default formats. (optional)
      "mkv",
      "mp4",
      "avi"
    ]
  }
  ```

- CLI

  ```shell
  >> autotitle -l 
  >> dc (aliases: 'detective-conan', 'detectiveconan')
  ```
